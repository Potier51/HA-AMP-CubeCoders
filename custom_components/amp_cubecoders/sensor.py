from __future__ import annotations

from homeassistant.components.sensor import SensorEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import DeviceInfo

from .const import DOMAIN


async def async_setup_entry(hass: HomeAssistant, entry, async_add_entities):
    """Set up AMP sensors from a config entry."""

    data = hass.data[DOMAIN][entry.entry_id]
    coordinator = data["coordinator"]

    entities = []

    # Pour chaque instance AMP, créer les entités
    for instance_id, instance_data in coordinator.data.items():
        info = instance_data["info"]
        name = info.get("FriendlyName", instance_id)

        entities.append(AMPStatusSensor(coordinator, instance_id, name))
        entities.append(AMPPlayerCountSensor(coordinator, instance_id, name))

    async_add_entities(entities)


# -------------------------------------------------------------------
# Base class for AMP sensors
# -------------------------------------------------------------------

class AMPSensorBase(SensorEntity):
    """Base class for AMP sensors."""

    def __init__(self, coordinator, instance_id: str, name: str):
        self.coordinator = coordinator
        self._instance_id = instance_id
        self._instance_name = name

    @property
    def should_poll(self):
        return False  # Coordinator gère les updates

    @property
    def available(self):
        return self._instance_id in self.coordinator.data

    @property
    def device_info(self) -> DeviceInfo:
        """Regroupe les entités par instance AMP."""
        return DeviceInfo(
            identifiers={(DOMAIN, self._instance_id)},
            name=f"AMP - {self._instance_name}",
            manufacturer="CubeCoders",
            model="AMP Instance",
        )

    async def async_update(self):
        """Forcer une mise à jour via le coordinator."""
        await self.coordinator.async_request_refresh()

    @property
    def data(self):
        """Accès rapide aux données de l’instance."""
        return self.coordinator.data[self._instance_id]


# -------------------------------------------------------------------
# Status Sensor
# -------------------------------------------------------------------

class AMPStatusSensor(AMPSensorBase):
    """Sensor indiquant le statut de l’instance."""

    @property
    def name(self):
        return f"{self._instance_name} - Status"

    @property
    def unique_id(self):
        return f"{self._instance_id}_status"

    @property
    def state(self):
        return self.data["status"].get("status", "unknown")


# -------------------------------------------------------------------
# Player Count Sensor
# -------------------------------------------------------------------

class AMPPlayerCountSensor(AMPSensorBase):
    """Sensor indiquant le nombre de joueurs connectés."""

    @property
    def name(self):
        return f"{self._instance_name} - Players"

    @property
    def unique_id(self):
        return f"{self._instance_id}_players"

    @property
    def state(self):
        players = self.data["players"].get("players", [])
        return len(players)
