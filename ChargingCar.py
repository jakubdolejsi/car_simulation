from random import random, uniform

import defines
from Stats import Stats

class ChargingCar:
    def __init__(self, env, station):
        self.env = env
        self.station = station
        self.charging_process = env.process(self.behavior(env))
        self.arrive_time = env.now
        self.end_time = None

    def behavior(self, env):

        with self.station.request() as charging_request:
            yield charging_request

            Stats.time_in_queue.append(env.now - self.arrive_time)

            yield env.timeout(uniform(1 * defines.MINUTEs, 2 * defines.MINUTEs))

            if random() > 0.555: # automobil nepodporuje rychlonabijeni
                if random() > 0.333:
                    yield env.timeout(25 * defines.MINUTEs)
                else:
                    yield env.timeout(46.875 * defines.MINUTEs)
            else: # automobil podporuje rychlonabijeni
                if random() > 0.416: # Elektromobily s rychlonabijenim, s casem nabijeni nad 30 minut (10-80% kapacity baterie)
                    yield env.timeout(40.3 * defines.MINUTEs)
                else: # Elektromobily s rychlonabijenim, a casem nabijeni do 30 minut (10-80% kapacity baterie)
                    yield env.timeout(26.6 * defines.MINUTEs) # Prumerna doba nabijeni pro tuto kategrii


            yield env.timeout(uniform(1 * defines.MINUTEs, 1.5 * defines.MINUTEs))

            self.end_time = env.now
            Stats.whole_process_duration.append(self.end_time - self.arrive_time)
