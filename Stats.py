import matplotlib.pyplot as plt

class Stats:
    whole_process_duration = []
    chosen_stations = []
    requests = []
    time_in_queue = []


    @classmethod
    def print_process_duration(cls):
        print("-- Average whole charing proces duration {0} minutes".format(round(sum(cls.whole_process_duration) / len(cls.whole_process_duration), 2)))
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
        print('-- Total charging request count during simulation: {0}'.format(len(cls.requests)))


    @classmethod
    def get_average_time_in_queue(cls):
        print("-- Average time in queue is {0} minutes".format(round(sum(cls.time_in_queue) / len(cls.time_in_queue), 2)))
        print("-- Max time in queue is {0} minutes".format(round(max(cls.time_in_queue),2)))

    @classmethod
    def get_time_in_queue_without_waiting(cls):
        no_waiting = cls.time_in_queue.count(0.0) / len(cls.time_in_queue) * 100
        print("-- Percentage of cars which charge without waiting in queue: {} %".format(round(no_waiting, 2)))
