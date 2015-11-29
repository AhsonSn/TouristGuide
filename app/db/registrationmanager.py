from app.db.models import Registration, User
from app import database


class RegistrationManager(object):
    @staticmethod
    def get_registration_count_by_tour_id(id_):
        return Registration.query.filter_by(tour_id=id_).count()

    @staticmethod
    def get_tour_users_email(tourid):
        list_of_id = database.session.query(Registration, "user_id").filter_by(tour_id=tourid).all()
        ret_list = []
        for id_ in list_of_id:
            ret_list.append(database.session.query(User, "email").filter_by(id=id_[1]).first()[1])

        return ret_list

    @staticmethod
    def delete_tour(tourid_):
        Registration.query.filter_by(tour_id=tourid_).delete()
