from .models import Experience


class ExperienceDAO(object):

    @staticmethod
    def get_experiences():
        """
        Return a list of Experiences from database.
        :return: list of Experiences
        """
        return Experience.query.all()

    @staticmethod
    def get_experience_id_by_name(name_):
        """
        Return the id of an experience
        :param name_: name of experience
        :return: experience id
        """

        return Experience.query.filter_by(name=name_).first().id

    @staticmethod
    def get_experience_by_id(id_):
        """
        Returs the id of an experience
        :param id_: name of experience
        :return: experience id
        """

        return Experience.query.get(id_)
