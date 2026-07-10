"""Test fixtures for hassd_relay."""

from __future__ import annotations

import pytest

pytest_plugins = ["pytest_homeassistant_custom_component"]


@pytest.fixture(autouse=True)
def auto_enable_custom_integrations(enable_custom_integrations):
    """Make HA load custom_components/hassd_relay during tests."""
    yield
