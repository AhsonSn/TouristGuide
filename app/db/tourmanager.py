from .models import Tour
from datetime import datetime
from app import database


class TourManager(object):

    def insert_tour(self, name, start_date, end_date, exp_id, tg_id, description, images="", dateformat="%Y-%m-%d %H:%M"):
        """
        Insert a new tour to database. The default date format is yyyy.mm.dd hh:mi, so date is a string. If you want to
        change date format, give the dateformat parameter.
        :param name: Tour name
        :param start_date: string of start date time of tour
        :param end_date: string of end date time of tour
        :param exp_id: experience id
        :param tg_id: tour guide id
        :param description: description of tour
        :param images: (Optional) tour images src
        :param dateformat: (Optional) a format string to start and end date.
        :return:
        """

        tour = Tour(name, exp_id, tg_id)
        tour.start_datetime = datetime.strptime(start_date, dateformat)
        tour.end_datetime = datetime.strptime(end_date, dateformat)
        tour.images = images
        tour.description = description
        database.session.add(tour)
        database.session.commit()

    def get_id_list_of_tours_by_date(self, start_date_, end_date_):
        """
        Return a list of tours name, and id tuple.
        :param start_date_: start date of query
        :param end_date_: end date of query
        :return: tuple list of name, and id
        """
        return database.session.query(Tour, "id").filter(Tour.start_datetime.between(start_date_, end_date_)).all()

    def get_list_of_tours_by_date(self, start_date_, end_date_):
        """
        Return a list of tours between dates.
        :param start_date_: start date of query
        :param end_date_: end date of query
        :return: tuple list of name, and id
        """
        return database.session.query(Tour).filter(Tour.start_datetime.between(start_date_, end_date_)).all()
