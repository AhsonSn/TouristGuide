from .usermanager import UserManager
from .tourmanager import TourManager
from .experiencemanager import ExperienceManager
from .registrationmanager import RegistrationManager


class DBFactory(object):

    def __init__(self):
        self.User = UserManager()
        self.Tour = TourManager()
        self.Experience = ExperienceManager()
        self.Registration = RegistrationManager()

    # Private member, please use get_instance.
    __instance = None

    @staticmethod
    def get_instance():
        if DBFactory.__instance is None:
            DBFactory.__instance = DBFactory()
            return DBFactory.__instance

        return DBFactory.__instance













