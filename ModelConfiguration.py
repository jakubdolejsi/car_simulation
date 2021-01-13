from __future__ import annotations

import configparser
import os
import defines
from Stats import Stats


class ModeConfiguration:
    """
    Configuration class for simulation model
    """

    __configuration: dict

    __default_values: dict = {
        'cars': 10_000,
        'chargers': 100,
        'sim_len': 7,
        'distance_per_charge': 294.25926
    }

    validated: bool = False

    def load(self) -> ModeConfiguration:
        """
        Load all configuration from config.ini file specified in config directory
        :rtype: ModeConfiguration
        """
        config = configparser.ConfigParser()
        config.read(os.path.join('config', 'config.ini'))

        dictionary = {}
        for section in config.sections():
            dictionary[section] = {}
            for option in config.options(section):
                try:
                    dictionary[section][option] = int(config.get(section, option))
                except ValueError as ve:
                    Stats.log(message="CONFIGURATION FILE IS NOT CORRECT!")
                    Stats.log(message=f"ERROR: {ve}")
                    exit(1)

        self.__configuration = dictionary['ModelArgs']
        return self

    def enable_default(self) -> ModeConfiguration:
        """
        Enable setting default values for model parameters
        :rtype: ModeConfiguration
        """
        for key, value in self.__default_values.items():
            if not key in self.__configuration:
                self.__configuration[key] = value
        self.validated = True
        return self

    def initialize(self) -> ModeConfiguration:
        """
        Initialize model with loaded parameters
        :rtype: ModeConfiguration
        """
        if not self.validated:
            Stats.log(message='\n*********** WARNING ***********\n')
            Stats.log(message='DEFAULT VALUES ARE NOT CONFIGURED\n')


        defines.AVERAGE_DISTANCE_10_80 = self.__configuration['distance_per_charge'] * 0.7
        defines.AVERAGE_DISTANCE_PER_CHARGE = self.__configuration['distance_per_charge']
        defines.CHARGING_STATIONS_COUNT = self.__configuration['chargers']
        defines.SIMULATION_LEN = self.__configuration['sim_len'] * 1 * defines.WEEKs
        defines.CHARGING_ON_PUBLIC_STATION_COUNT = self.__configuration['cars']
        defines.CHARGERS_IN_CITY_CENTRE = defines.CHARGING_STATIONS_COUNT * 0.65
        defines.CHARGERS_OUTSIDE_CITY_CENTRE = defines.CHARGING_STATIONS_COUNT * 0.35

        Stats.log(message=f'\nModel loaded with following configuration')
        Stats.log(message=f'{self.__configuration}\n')

        return self
