from app.db.models import Registration


class RegistrationManager(object):
    def get_registration_count_by_tour_id(self, id_):
        return Registration.query.filter_by(tour_id=id_).count()
