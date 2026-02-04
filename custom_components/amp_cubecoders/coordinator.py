from __future__ import annotations

import logging
from datetime import timedelta

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .api import AMPApi
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)


class AMPDataCoordinator(DataUpdateCoordinator):
    """Coordinator centralisant les données AMP."""

    def __init__(self, hass: HomeAssistant, api: AMPApi, scan_interval: int):
        """Initialise le coordinator avec un intervalle dynamique."""
        super().__init__(
            hass,
            _LOGGER,
            name="CubeCoders AMP Coordinator",
            update_interval=timedelta(seconds=scan_interval),
        )

        self.api = api

    async def _async_update_data(self):
        """Récupère les données depuis AMP."""

        try:
            instances = await self.api.list_instances()
            instance_list = instances.get("instances", [])

            data = {}

            for inst in instance_list:
                instance_id = inst.get("InstanceID")
                if not instance_id:
                    continue

                status = await self.api.get_status(instance_id)
                players = await self.api.get_players(instance_id)

                data[instance_id] = {
                    "info": inst,
                    "status": status,
                    "players": players,
                }

            return data

        except Exception as err:
            raise UpdateFailed(f"Erreur lors de la mise à jour AMP: {err}") from err
