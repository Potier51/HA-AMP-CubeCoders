from __future__ import annotations

import aiohttp
import async_timeout
import logging

_LOGGER = logging.getLogger(__name__)


class AMPApi:
    """Simple async API wrapper for CubeCoders AMP.

    Authenticate using username/password (not API key).
    """

    def __init__(self, host: str, username: str, password: str):
        self._host = host.rstrip("/")
        self._username = username
        self._password = password

    async def _post(self, endpoint: str, payload: dict | None = None) -> dict:
        """Internal helper to send POST requests to AMP."""
        url = f"http://{self._host}/API/{endpoint}"

        data = {"Username": self._username, "Password": self._password}
        if payload:
            data.update(payload)

        try:
            async with async_timeout.timeout(10):
                async with aiohttp.ClientSession() as session:
                    async with session.post(url, json=data) as resp:
                        if resp.status != 200:
                            text = await resp.text()
                            _LOGGER.error(
                                "AMP API error %s on %s: %s", resp.status, endpoint, text
                            )
                            resp.raise_for_status()

                        return await resp.json()

        except Exception as err:
            _LOGGER.error("Error calling AMP endpoint %s: %s", endpoint, err)
            raise

    # ---------------------------------------------------------
    # Public API methods
    # ---------------------------------------------------------

    async def list_instances(self) -> dict:
        """Return the list of AMP instances."""
        return await self._post("ADSModule/ListInstances")

    async def get_status(self, instance_id: str) -> dict:
        """Return the status of a specific instance."""
        return await self._post(
            "ADSModule/GetStatus",
            {"InstanceID": instance_id},
        )

    async def get_players(self, instance_id: str) -> dict:
        """Return the list of connected players for an instance."""
        return await self._post(
            "ADSModule/GetPlayerList",
            {"InstanceID": instance_id},
        )
