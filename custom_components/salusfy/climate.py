"""
Adds support for the Salus Thermostat units.
"""
import logging

import homeassistant.helpers.config_validation as cv
import voluptuous as vol

from homeassistant.const import (
    CONF_PASSWORD,
    CONF_USERNAME,
    CONF_ID,
)

from custom_components.salusfy.thermostat_entity import ThermostatEntity
from custom_components.salusfy.web_client import WebClient

from homeassistant.components.climate import PLATFORM_SCHEMA

__version__ = "0.0.1"

_LOGGER = logging.getLogger(__name__)

DEFAULT_NAME = "Salus Thermostat"

CONF_NAME = "name"


PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
        vol.Required(CONF_USERNAME): cv.string,
        vol.Required(CONF_PASSWORD): cv.string,
        vol.Required(CONF_ID): cv.string,
    }
)


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the E-Thermostat platform."""
    name = config.get(CONF_NAME)
    username = config.get(CONF_USERNAME)
    password = config.get(CONF_PASSWORD)
    id = config.get(CONF_ID)

    _LOGGER.info('Registering SalusThermostat climate entity...')

    web_client = WebClient(username, password, id)

    add_entities(
        [ThermostatEntity(name, web_client)]
    )