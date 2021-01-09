# Exit codes
EXIT_SUCCESS = 0
EXIT_FAIL =  -1

# Basic time units convert (to seconds)
WEEKs = 7 * 24 * 60 * 1.0
DAYs = 24 * 60 * 1.0
HOURs = 60 * 1.0
MINUTEs = 1.0
SECONDs = 1.0 / 60.0

# Night len in minutes
NIGHT_LEN = 480

# Percentage of cars that mostly charge on charger in city centre
IN_CITY_CENTRE = 0.7

# Percentage of cars that mostly charge on charger outside city centre
OUT_CITY_CENTRE = 1 - IN_CITY_CENTRE

# Convert days to seconds
daysToSeconds = lambda x : x * 86400


def is_night(sim_time):
    sim_time = (sim_time % DAYs)
    return not sim_time > NIGHT_LEN


# Number of cars that mostly charge on public charging station (not at home, work etc.)
CHARGING_ON_PUBLIC_STATION_COUNT = None

# Average distance car distance per 1 charge (in Kilometres)

AVERAGE_DISTANCE_PER_CHARGE = 294.25926

# Average car distance 10-80% battery capacity

AVERAGE_DISTANCE_10_80 = AVERAGE_DISTANCE_PER_CHARGE * 0.7

# Average car distance per one day

AVERAGE_DISTANCE_PER_DAY =  28.68

# Count of charging stations in City (Brno)
CHARGING_STATIONS_COUNT = None

# Simulation duration
SIMULATION_LEN = None

# Number of charging stations, that are located in city centre (35%)
CHARGERS_IN_CITY_CENTRE = None

# Number of charging stations, that are located outside city centre (65%)
CHARGERS_OUTSIDE_CITY_CENTRE = None

arriveTimesPerNight = 0
arriveTimesPerDay = 0

def CountArriveTimes():
    averageDaysPerCharge = (daysToSeconds(AVERAGE_DISTANCE_10_80 / AVERAGE_DISTANCE_PER_DAY)/ CHARGING_ON_PUBLIC_STATION_COUNT)
    averageCarsCountPerDay = (daysToSeconds(1) / averageDaysPerCharge)

    inNightPerHour = (averageCarsCountPerDay * 0.113 / 8)
    inDayPerHour = (averageCarsCountPerDay * 0.887 / 16)
    global arriveTimesPerDay, arriveTimesPerNight
    arriveTimesPerNight = ((3600 / inNightPerHour) * SECONDs)
    arriveTimesPerDay = ((3600 / inDayPerHour) * SECONDs)

    print('-- Average time between arrives in 06:00 - 22:00 (DAY) - {0} minutes.'.format(round(arriveTimesPerDay,2)))
    print('-- Average time between arrives in 22:00 - 06:00 (NIGHT) - {0} minutes.'.format(round(arriveTimesPerNight, 2)))
