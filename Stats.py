import matplotlib.pyplot as plt

class Stats:
    whole_process_duration = []
    chosen_stations = []
    reqests = []


    @classmethod
    def print_process_duration(cls):
        print("-- Average whole charing proces duration {0} minutes".format(round(sum(cls.whole_process_duration) / len(cls.whole_process_duration),2)))
        print("-- Max whole charing proces duration {0} minutes".format(round(max(cls.whole_process_duration),2)))
        print("-- Min whole charing proces duration {0} minutes".format(round(min(cls.whole_process_duration),2)))
        print("")


    @classmethod
    def print_station_info(cls):
        n, bins, patches = plt.hist(cls.chosen_stations)
        plt.xlabel('Charger number')
        plt.ylabel('Number of picks the charger')
        plt.title("Histogram")
        plt.savefig('ChargersPicksHistogram.png')

    @classmethod
    def request_count(cls):
        print('-- Total charging request count during simulation: {0}'.format(len(cls.reqests)))
