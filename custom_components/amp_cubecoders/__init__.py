from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

from .const import DOMAIN, DEFAULT_SCAN_INTERVAL
from .api import AMPApi
from .coordinator import AMPDataCoordinator

PLATFORMS = ["sensor"]


async def async_setup(hass: HomeAssistant, config: ConfigType):
    """YAML setup (unused)."""
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up CubeCoders AMP from a config entry."""

    host = entry.data["host"]
    username = entry.data.get("username")
    password = entry.data.get("password")

    # Récupération de l’intervalle dynamique
    scan_interval = entry.options.get("scan_interval", DEFAULT_SCAN_INTERVAL)

    api = AMPApi(host, username, password)
    coordinator = AMPDataCoordinator(hass, api, scan_interval)

    await coordinator.async_config_entry_first_refresh()

    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = {
        "api": api,
        "coordinator": coordinator,
    }

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload a config entry."""

    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)

    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok
