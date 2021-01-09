from __future__ import annotations

import configparser
import os
import defines


class ModeConfiguration:
    """
    Configuration class for simulation model
    """

    __configuration: dict

    __default_values: dict = {
        'cars': 10_000,
        'chargers': 100,
        'sim_len': 7
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
                    print('CONFIGURATION FILE IS NOT CORRECT!')
                    print(f'ERROR: {ve}')
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
            print('\n*********** WARNING ***********\n')
            print('DEFAULT VALUES ARE NOT CONFIGURED\n')


        defines.CHARGING_STATIONS_COUNT = self.__configuration['chargers']
        defines.SIMULATION_LEN = self.__configuration['sim_len'] * 1 * defines.WEEKs
        defines.CHARGING_ON_PUBLIC_STATION_COUNT = self.__configuration['cars']
        defines.CHARGERS_IN_CITY_CENTRE = defines.CHARGING_STATIONS_COUNT * 0.65
        defines.CHARGERS_OUTSIDE_CITY_CENTRE = defines.CHARGING_STATIONS_COUNT * 0.35

        print(f'\nModel loaded with following configuration')
        print(f'{self.__configuration}\n')

        return self
