import pytest

from salusfy import climate
from .config_adapter import ConfigAdapter
from .entity_registry import EntityRegistry

from . import config


def test_entity_is_registered():
    registry = EntityRegistry()
    config_adapter = ConfigAdapter(config)
    climate.setup_platform(None, config_adapter, add_entities=registry.register, discovery_info=None)
    
    assert len(registry.entities) == 1