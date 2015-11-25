from .models import Experience


class ExperienceManager(object):

    def get_experiences(self):
        """
        Return a list of Experience from database.
        :return: list of Experience
        """
        return Experience.query.all()