import simpy

import defines
from RequestGenerator import RequestGenerator
from Stats import Stats


class Simulation:
    def __init__(self, simulation_end):
        self.simulation_end = simulation_end

    def printStats(self):
        print("\n{0} STATS {0}\n".format(12*'-'))
        Stats.print_process_duration()
        Stats.print_station_info()
        Stats.request_count()

    def run(self):
        defines.CountArriveTimes()
        env = simpy.Environment()
        RequestGenerator(env)
        print("\n-- Simulation run started - Simulation time {} minutes... --".format(env.now))
        env.run(until=self.simulation_end)
        print("\n-- Simulation run finished - Simulation time {} minutes... --".format(env.now))
        self.printStats()


