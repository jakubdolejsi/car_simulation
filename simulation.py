import simpy

import defines
from RequestGenerator import RequestGenerator
from Stats import Stats


class Simulation:
    def __init__(self, simulation_end):
        self.simulation_end = simulation_end

    def printStats(self):
        Stats.log(message="\n{0} STATS {0}\n".format(12 * '-'))
        Stats.print_process_duration()
        Stats.print_station_info()
        Stats.request_count()
        Stats.get_average_time_in_queue()
        Stats.get_time_in_queue_without_waiting()

    def run(self):
        defines.CountArriveTimes()
        env = simpy.Environment()
        RequestGenerator(env)
        Stats.log(message="\n-- Simulation run started - Simulation time {} minutes... --".format(env.now))
        env.run(until=self.simulation_end)
        Stats.log(message="\n-- Simulation run finished - Simulation time {} minutes... --".format(env.now))
        self.printStats()
