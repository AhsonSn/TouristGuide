from app.db import dbfactory
from app.db.dbfactory import DBFactory


class Statistics(object):
    def __init__(self):
        self.statistics_manager = DBFactory.get_instance().Statistic

    def get_stat_by_registered_user(self, start_date, end_date):
        """
        Queries the tours from the database, then returns a tuple that contains labels and data, which are
        required to display the carts.
        :param start_date: the begin of the time interval
        :param end_date: the end of the time interval
        :return: a tuple that contains: labels, data
        """
        tours = self.statistics_manager.get_tours(start_date, end_date)
        labels = [str(name) for (name, count) in tours]
        data = [count for (name, count) in tours]
        return labels, data

    def get_stat_by_tourguide(self, start_date, end_date):
        """
        Queries the tour guides from the database, then returns a tuple that contains labels and data, which are
        required to display the charts. The data is represents the cardinality of the guided tours.
        :param start_date: the begin of the time interval
        :param end_date: the end of the time interval
        :return: a tuple that contains: labels, data
        """
        tourguides = self.statistics_manager.get_static_from_tour_guide(start_date, end_date)
        labels = [str(name) for (name, count) in tourguides]
        data = [count for (name, count) in tourguides]
        return labels, data

    def get_stat_by_tourguide_popularity(self, start_date, end_date):
        """
        Queries the tour guides from the database, then returns a tuple that contains labels and data, which are
        required to display the charts. The data is represents the popularity of the tour guide.
        :param start_date:
        :param end_date:
        :return: a tuple that contains: labels, data
        """
        tourguides = self.statistics_manager.get_static_from_tour_guide_popularity(start_date, end_date)
        labels = [str(name) for (name, count) in tourguides]
        data = [count for (name, count) in tourguides]
        return labels, data

