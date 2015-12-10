from datetime import datetime

from app import database
from app.db.models import Registration, User

class RegistrationManager(object):
    @staticmethod
    def get_registration_count_by_tour_id(id_):
        return Registration.query.filter_by(tour_id=id_).count()

    @staticmethod
    def get_tour_users_email(tourid):
        list_of_id = database.session.query(Registration, "user_id").filter_by(
            tour_id=tourid).all()
        ret_list = []
        for id_ in list_of_id:
            ret_list.append(database.session.query(User, "email").filter_by(
                id=id_[1]).first()[1])

        return ret_list

    @staticmethod
    def get_registrations_of_user(user):
        return Registration.query.filter_by(user_id=user.id).all()

    @staticmethod
    def register_user(user, tour):
        registration = Registration.query.filter_by(
            user=user, tour=tour).first()

        active_registration = Registration.query.filter(Registration.user == user).all()
        
        ontour = False

        for reg in active_registration:
            if reg.tour.start_datetime <= tour.start_datetime <= reg.tour.end_datetime:
                ontour = True
                break

        ontour2 = False
        
        for reg in active_registration:
            if reg.tour.start_datetime <= tour.end_datetime <= reg.tour.end_datetime:
                ontour2 = True
                break

        if registration:
            return 1
        elif ontour:
            return 2
        elif ontour2:
            return 3
        else:
            database.session.add(
                Registration(user, tour, datetime.now(), False))
            database.session.commit()
            return 0

    @staticmethod
    def unregister_user(user_id, tour_id):
        Registration.query.filter_by(tour_id=tour_id, user_id=user_id).delete()
        database.session.commit()
