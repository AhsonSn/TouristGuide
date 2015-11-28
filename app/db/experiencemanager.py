from .models import Experience


class ExperienceManager(object):

    @staticmethod
    def get_experiences():
        """
        Return a list of Experiences from database.
        :return: list of Experiences
        """
        return Experience.query.all()

    @staticmethod
    def get_experience_by_name(name_):
        """
        Return the id of an experience
        :param name_: name of experience
        :return: experience id
        """

        return Experience.query.filter_by(name=name_).first().id
