from random import random

from simpy import Environment, Resource
import defines
from ChargingCar import ChargingCar
from Stats import Stats


class RequestGenerator:

    def __init__(self, env):
        self.env = env
        self.generator_process  = env.process(self.generate_request(env))
        self.resource_list = [Resource(env, capacity=1) for _ in range(defines.CHARGING_STATIONS_COUNT)]

    def generate_request(self, env: Environment):
        progress = 1
        step_size = defines.SIMULATION_LEN / 100
        tmp_step = step_size
        while True:
            Stats.requests.append(1)
            station_index = self.choose_station()

            station = self.resource_list[station_index]
            Stats.chosen_stations.append(station_index)


            if env.now > tmp_step:
                Stats.log(message=f'Progress {progress} %', target='stdout')
                tmp_step = tmp_step + step_size
                progress = progress + 1

            ChargingCar(env, station)


            is_night = defines.is_night(env.now)
            if is_night: # If is night
                yield env.timeout(defines.arriveTimesPerNight)
            else:
                yield env.timeout(defines.arriveTimesPerDay)

    def choose_station(self):
        if random() > defines.IN_CITY_CENTRE:
            return int(random() * defines.CHARGERS_OUTSIDE_CITY_CENTRE + defines.CHARGERS_IN_CITY_CENTRE - 1)
        else:
            return int( random() * defines.CHARGERS_IN_CITY_CENTRE)

