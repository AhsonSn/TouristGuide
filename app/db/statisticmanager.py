from app.db.tourmanager import TourDAO
from app.db.registrationmanager import RegistrationDAO
from app.db.usermanager import UserDAO

class StatisticDAO(object):
    @staticmethod
    def get_tours(start_date, end_date):
        """
        Return a list of tuple.

        Tuple contains a name and number of registered member. The return list is ordered.
        You can find an example to call this method in testdatabase.py file.
        :param start_date: String that represent a date like this: "2015-09-01"
        :param end_date: same as start_date
        :return:
        """
        list_of_tours = TourDAO.get_id_list_of_tours_by_date(start_date, end_date)

        d = dict()
        for name, id in list_of_tours:
            d[id] = RegistrationDAO.get_registration_count_by_tour_id(id)

        return_list = []
        for name, id in list_of_tours:
            return_list.append((name, d[id]))

        return_list = sorted(return_list, key=StatisticDAO.get_key, reverse=True)

        return return_list

    @staticmethod
    def get_key(item):
        return item[1]

    @staticmethod
    def get_static_from_tour_guide(start_date, end_date):
        """
        Return an descending ordered list from tourguide's tours between dates.

        You can find an example to call this method in testdatabase.py file.
        :param start_date: String that represent a date like this: "2015-09-01"
        :param end_date: same as start_date
        :return:
        """
        list_of_tours = TourDAO.get_list_of_tours_between_dates(start_date, end_date)

        d = dict()

        for tour in list_of_tours:
            if tour.tour_guide_id in d:
                d[tour.tour_guide_id] += 1
            else:
                d[tour.tour_guide_id] = 1

        return_list = []
        for key, value in d.items():
            return_list.append((UserDAO.get_user_by_id(key).fullname, value))

        return_list = sorted(return_list, key=StatisticDAO.get_key, reverse=True)

        return return_list

    @staticmethod
    def get_static_from_tour_guide_popularity(start_date, end_date):
        """
        Return an descending ordered list from tourguide's tours popularity between dates.

        You can find an example to call this method in testdatabase.py file.
        :param start_date: String that represent a date like this: "2015-09-01"
        :param end_date: same as start_date
        :return:
        """
        list_of_tours = TourDAO.get_list_of_tours_between_dates(start_date, end_date)

        d = dict()
        for tour in list_of_tours:
            if tour.tour_guide_id in d:
                d[tour.tour_guide_id] += RegistrationDAO.get_registration_count_by_tour_id(tour.id)
            else:
                d[tour.tour_guide_id] = RegistrationDAO.get_registration_count_by_tour_id(tour.id)

        return_list = []
        for key, value in d.items():
            return_list.append((UserDAO.get_user_by_id(key).fullname, value))

        return_list = sorted(return_list, key=StatisticDAO.get_key, reverse=True)

        return return_list

