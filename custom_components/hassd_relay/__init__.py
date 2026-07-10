"""hassd Relay integration.

Stub scaffold. This integration is intended to expose Home Assistant services
that relay into the palantir `hassd` daemon, mirroring `labd-relay`. No services
are defined yet — `async_setup_entry` only registers the (empty) config entry so
the integration loads cleanly.
"""

from __future__ import annotations

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    # Stub: no services registered yet. Track the entry so unload is symmetric.
    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = entry
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    entries: dict[str, ConfigEntry] = hass.data.get(DOMAIN, {})
    entries.pop(entry.entry_id, None)
    if not entries:
        hass.data.pop(DOMAIN, None)
    return True
