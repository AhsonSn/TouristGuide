from .models import Tour
from datetime import datetime
from app import database


class TourManager(object):

    @staticmethod
    def insert_tour(name, start_date, end_date, exp_id, tg_id, description, images="", dateformat="%Y-%m-%d %H:%M"):
        """
        Insert a new tour into the database. The default date format is yyyy.mm.dd hh:mi, as a string.
        If you want to change it, pass the dateformat parameter.
        :param name: Tour name
        :param start_date: string of start date time of tour
        :param end_date: string of end date time of tour
        :param exp_id: experience id
        :param tg_id: tour guide id
        :param description: description of tour
        :param images: (Optional) tour images src
        :param dateformat: (Optional) a format string to start and end date.
        """

        tour = Tour(name, exp_id, tg_id)
        tour.start_datetime = datetime.strptime(start_date, dateformat)
        tour.end_datetime = datetime.strptime(end_date, dateformat)
        tour.images = images
        tour.description = description
        database.session.add(tour)
        database.session.commit()

    @staticmethod
    def get_id_list_of_tours_by_date(start_date_, end_date_):
        """
        Return a list of tour name and id tuples.
        :param start_date_: start date of query
        :param end_date_: end date of query
        :return: tuple list of name, and id
        """
        return database.session.query(Tour, "id").filter(Tour.start_datetime.between(start_date_, end_date_)).all()

    @staticmethod
    def get_list_of_tours_by_date(start_date_, end_date_):
        """
        Return a list of tours between dates.
        :param start_date_: start date of query
        :param end_date_: end date of query
        :return: tuple list of name, and id
        """
        return database.session.query(Tour).filter(Tour.start_datetime.between(start_date_, end_date_)).all()

    @staticmethod
    def get_page_of_tours(current_page, per_page, order_by):
        """
        Return a page of tours.
        :param current_page: current_page of query
        :param per_page: items per page
        :param order_by: order by this property
        :return: tuple list of name, and id
        """

        if order_by == 1:
            order = Tour.start_datetime
        elif order_by == 2:
            order = Tour.name
        else:
            order = Tour.experience_id

        return Tour.query.order_by(order).paginate(current_page, per_page=per_page)
