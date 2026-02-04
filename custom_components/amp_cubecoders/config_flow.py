from __future__ import annotations

import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import FlowResult

from .const import (
    DOMAIN,
    DEFAULT_SCAN_INTERVAL,
)

from .api import AMPApi


# ---------------------------------------------------------
# Helpers
# ---------------------------------------------------------

async def validate_connection(hass: HomeAssistant, host: str, api_key: str):
    """Test la connexion AMP et retourne la liste des instances."""
    api = AMPApi(host, api_key)
    try:
        data = await api.list_instances()
        return data.get("instances", [])
    except Exception as err:
        raise ValueError(f"Impossible de se connecter à AMP: {err}")


# ---------------------------------------------------------
# Config Flow principal
# ---------------------------------------------------------

class AMPConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Flow de configuration pour CubeCoders AMP."""

    VERSION = 1

    def __init__(self):
        self.host = None
        self.api_key = None
        self.instances = None

    async def async_step_user(self, user_input=None) -> FlowResult:
        """Étape 1 : demander IP + API Key."""
        errors = {}

        if user_input is not None:
            host = user_input["host"]
            api_key = user_input["api_key"]

            try:
                instances = await validate_connection(self.hass, host, api_key)
                self.host = host
                self.api_key = api_key
                self.instances = instances
                return await self.async_step_select_instances()

            except ValueError:
                errors["base"] = "cannot_connect"

        schema = vol.Schema(
            {
                vol.Required("host"): str,
                vol.Required("api_key"): str,
            }
        )

        return self.async_show_form(
            step_id="user",
            data_schema=schema,
            errors=errors,
        )

    async def async_step_select_instances(self, user_input=None) -> FlowResult:
        """Étape 2 : sélectionner les instances à intégrer."""
        errors = {}

        # Construire la liste des choix
        instance_choices = {
            inst["InstanceID"]: inst.get("FriendlyName", inst["InstanceID"])
            for inst in self.instances
        }

        if user_input is not None:
            selected = user_input["instances"]
            scan_interval = user_input["scan_interval"]

            return self.async_create_entry(
                title=f"CubeCoders AMP ({self.host})",
                data={
                    "host": self.host,
                    "api_key": self.api_key,
                },
                options={
                    "instances": selected,
                    "scan_interval": scan_interval,
                },
            )

        schema = vol.Schema(
            {
                vol.Required("instances"): vol.All(
                    cv.ensure_list,
                    [vol.In(instance_choices)],
                ),
                vol.Required("scan_interval", default=DEFAULT_SCAN_INTERVAL): vol.All(
                    int, vol.Range(min=5, max=3600)
                ),
            }
        )

        return self.async_show_form(
            step_id="select_instances",
            data_schema=schema,
            errors=errors,
        )

    @staticmethod
    def async_get_options_flow(config_entry):
        return AMPOptionsFlow(config_entry)


# ---------------------------------------------------------
# Options Flow (modifier après installation)
# ---------------------------------------------------------

class AMPOptionsFlow(config_entries.OptionsFlow):
    """Flow pour modifier les options après installation."""

    def __init__(self, entry):
        self.entry = entry

    async def async_step_init(self, user_input=None) -> FlowResult:
        """Écran principal des options."""
        return await self.async_step_edit()

    async def async_step_edit(self, user_input=None) -> FlowResult:
        """Modifier les instances et l’intervalle."""
        errors = {}

        # Récupérer les valeurs actuelles
        current_instances = self.entry.options.get("instances", [])
        current_interval = self.entry.options.get("scan_interval", DEFAULT_SCAN_INTERVAL)

        # Re-tester la connexion pour récupérer la liste des instances
        api = AMPApi(self.entry.data["host"], self.entry.data["api_key"])
        try:
            data = await api.list_instances()
            instances = data.get("instances", [])
        except Exception:
            errors["base"] = "cannot_connect"
            instances = []

        instance_choices = {
            inst["InstanceID"]: inst.get("FriendlyName", inst["InstanceID"])
            for inst in instances
        }

        if user_input is not None:
            return self.async_create_entry(
                title="",
                data={
                    "instances": user_input["instances"],
                    "scan_interval": user_input["scan_interval"],
                },
            )

        schema = vol.Schema(
            {
                vol.Required("instances", default=current_instances): vol.All(
                    cv.ensure_list,
                    [vol.In(instance_choices)],
                ),
                vol.Required("scan_interval", default=current_interval): vol.All(
                    int, vol.Range(min=5, max=3600)
                ),
            }
        )

        return self.async_show_form(
            step_id="edit",
            data_schema=schema,
            errors=errors,
        )
