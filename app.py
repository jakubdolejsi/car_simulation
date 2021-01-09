import defines
from simulation import Simulation
from ModelConfiguration import ModeConfiguration

def main():
    ModeConfiguration().load().enable_default().initialize()
    Simulation(simulation_end=defines.SIMULATION_LEN).run()

if __name__ == '__main__':
    main()











