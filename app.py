import defines
from simulation import Simulation
import argparse

def parseArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cars", required=True, type=int, help="Number of cars that mostly charge on public charging station (not at home, work etc.)")
    parser.add_argument("--chargers", required=True, type=int, help="Count of charging stations in City (Brno)")
    parser.add_argument("--simlen", required=True, type=int, help="Simulation lenght in weeks")
    return parser.parse_args()

def initBaseSimData(argumets):
    defines.CHARGING_STATIONS_COUNT = argumets.chargers
    defines.SIMULATION_LEN = argumets.simlen * 1 * defines.WEEKs
    defines.CHARGING_ON_PUBLIC_STATION_COUNT = argumets.cars
    defines.CHARGERS_IN_CITY_CENTRE = defines.CHARGING_STATIONS_COUNT * 0.65
    defines.CHARGERS_OUTSIDE_CITY_CENTRE = defines.CHARGING_STATIONS_COUNT * 0.35

def main():
    argumets = parseArguments()
    initBaseSimData(argumets)
    simulation = Simulation(simulation_end=defines.SIMULATION_LEN)
    simulation.run()

if __name__ == '__main__':
    main()











