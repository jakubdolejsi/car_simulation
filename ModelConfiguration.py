import configparser
import os

import defines


class ModeConfiguration:

    __configuration: dict
    __default_values = {
        'cars': 10_000,
        'chargers': 100,
        'sim_len': 7
    }
    validated = False

    def load(self):
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

    def enable_default(self):

        for key, value in self.__default_values.items():
            if not key in self.__configuration:
                self.__configuration[key] = value
        self.validated = True
        return self

    def initialize(self):
        if not self.validated:
            print('\n*********** WARNING ***********\n')
            print('DEFAULT VALUES ARE NOT CONFIGURED\n')


        defines.CHARGING_STATIONS_COUNT = self.__configuration['chargers']
        defines.SIMULATION_LEN = self.__configuration['sim_len'] * 1 * defines.WEEKs
        defines.CHARGING_ON_PUBLIC_STATION_COUNT = self.__configuration['cars']
        defines.CHARGERS_IN_CITY_CENTRE = defines.CHARGING_STATIONS_COUNT * 0.65
        defines.CHARGERS_OUTSIDE_CITY_CENTRE = defines.CHARGING_STATIONS_COUNT * 0.35
        print(self.__configuration)
