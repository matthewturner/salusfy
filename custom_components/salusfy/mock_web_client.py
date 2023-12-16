"""
Adds support for the Salus Thermostat units.
"""
import logging

from . import (
    State,
    HVAC_MODE_HEAT,
    HVAC_MODE_OFF,
    STATE_ON,
    STATE_OFF
)


_LOGGER = logging.getLogger(__name__)

class MockWebClient:
    """Mocks requests to Salus web application"""

    def __init__(self):
        """Initialize the client."""
        self._state = State()
        self._state.target_temperature = 20
        self._state.current_temperature = 15
        self._state.frost = 10


    def set_temperature(self, temperature):
        """Set new target temperature."""
        
        _LOGGER.info("Setting temperature to %.1f...", temperature)
        
        self._state.target_temperature = temperature


    def set_hvac_mode(self, hvac_mode):
        """Set HVAC mode, via URL commands."""
        
        _LOGGER.info("Setting the HVAC mode to %s...", hvac_mode)

        if hvac_mode == HVAC_MODE_OFF:
            self._state.current_operation_mode = STATE_OFF
        elif hvac_mode == HVAC_MODE_HEAT:
            self._state.current_operation_mode = STATE_ON


    def get_state(self):
        """Retrieves the mock status"""
        return self._state
