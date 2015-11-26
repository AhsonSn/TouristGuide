

class StatisticManager(object):
    def __init__(self, regisration_manager, tour_manager):
        self.regman = regisration_manager
        self.tourman = tour_manager

    def get_tours(self, start_date, end_date):
        """
        Return a list of tuple.

        Tuple contains a name and number of registered member. The return list is ordered.
        :param start_date: start date of statistic
        :param end_date: end date of statistic
        :return: Sorted list of tuple
        """
        list_of_tours = self.tourman.get_id_list_of_tours_by_date(start_date, end_date)

        d = dict()
        for name, id in list_of_tours:
            d[id] = self.regman.get_registration_count_by_tour_id(id)

        return_list = []
        for name, id in list_of_tours:
            return_list.append((name, d[id]))

        sorted(return_list, key=self.get_key)

        return return_list

    def get_key(self, item):
        return item[1]