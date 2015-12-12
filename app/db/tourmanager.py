from datetime import datetime

from sqlalchemy import update, func

from app import database
from .models import Tour
from .registrationmanager import RegistrationDAO
from ..basic.models import UploadManager


class TourDAO(object):
    @staticmethod
    def insert_tour(form):
        """
        Insert a new tour into the database. The default date format is yyyy.mm.dd hh:mi, as a string.
        If you want to change it, pass the dateformat parameter.
        :param form: the form
        """

        tour = Tour(form.data)
        tour.images = UploadManager.upload_tour_images()
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
        return database.session.query(Tour, "id").filter(
                Tour.start_datetime.between(start_date_, end_date_)).all()

    @staticmethod
    def get_list_of_tours_between_dates(start_date_, end_date_):
        return database.session.query(Tour).filter(
                Tour.start_datetime.between(start_date_, end_date_)).all()

    @staticmethod
    def get_list_of_tours_by_date(start_date_):
        """
        Return a list of tours whose start date is equal to start_date_.
        :param start_date_: start date of query
        :return: tuple list of name, and id
        """
        return database.session.query(Tour).filter(
                func.date(Tour.start_datetime) == start_date_).all()

    @staticmethod
    def get_list_of_tours_by_place(place):
        """
        Return a list of tours whose place is equal to place.
        :param place: start date of query
        :return: tuple list of name, and id
        """
        return database.session.query(Tour).filter(
                func.lower(Tour.place) == func.lower(place)).all()

    @staticmethod
    def get_list_of_tours_by_place_and_date(place, date):
        """
        Return a list of tours whose place is equal to place and
        start date is equal to start_date_.
        :param place: place of tour
        :param date: start date of query
        :return: tuple list of name, and id
        """
        return database.session.query(Tour).filter(
                func.lower(Tour.place) == func.lower(place),
                func.date(Tour.start_datetime) == date
        ).all()

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

        return Tour.query.order_by(order).paginate(
                current_page, per_page=per_page
        )

    @staticmethod
    def get_tour_by_id(tour_id):
        return Tour.query.get(tour_id)

    @staticmethod
    def delete_tour(tour_id):
        """
        Delete tour by id.
        :param tour_id: id of tour.
        :return: list of registered user's email.
        """
        l = RegistrationDAO.get_tour_users_email(tour_id)
        RegistrationDAO.delete_tour(tour_id)

        Tour.query.filter_by(id=tour_id).delete()
        database.session.commit()
        return l

    @staticmethod
    def delay_tour(tour_id, start_date_, end_date_):
        up = update(Tour).where(Tour.id == tour_id).values(
                start_datetime=datetime.strptime(start_date_, "%Y-%m-%d %H:%M"),
                end_datetime=datetime.strptime(end_date_, "%Y-%m-%d %H:%M"))

        database.session.execute(up)
        database.session.commit()

        return RegistrationDAO.get_tour_users_email(tour_id)

    @staticmethod
    def set_prices(list_of_tour):
        for tour in list_of_tour:
            up = update(Tour).where(Tour.id == tour.id).values(price=tour.price)
            database.session.execute(up)
            database.session.commit()

        return True

    @staticmethod
    def update_images(tour, images):
        database.session.execute(
                update(Tour).where(Tour.id == tour.id).values(images=images)
        )
        database.session.commit()

    @staticmethod
    def update_tour(current_tour, form):
        database.session.execute(
                update(Tour).where(Tour.id == current_tour.id).values(
                        name=form.name.data,
                        place=form.place.data,
                        start_datetime=form.start_date.data,
                        end_datetime=form.end_date.data,
                        experience_id=form.experience.data,
                        tour_guide_id=form.tour_guide.data,
                        description=form.description.data,
                        price=form.price.data
                )
        )
        database.session.commit()

        return True
