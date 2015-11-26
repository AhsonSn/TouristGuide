from .models import Experience


class ExperienceManager(object):

    def get_experiences(self):
        """
        Return a list of Experience from database.
        :return: list of Experience
        """
        return Experience.query.all()

    def get_experience_by_name(self, name_):
        """
        Return the id of experience
        :param name: name of experience
        :return: experience id
        """

        return Experience.query.filter_by(name=name_).first().id
