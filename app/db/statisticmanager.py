


class StatisticManager(object):
    def __init__(self, regisration_manager, tour_manager):
        self.regman = regisration_manager
        self.tourman = tour_manager

    def get_tours(self, start_date, end_date):
        list_of_tours = self.tourman.get_id_list_of_tours_by_date(start_date, end_date)
        return_list = []
        for x in list_of_tours:
            pass


