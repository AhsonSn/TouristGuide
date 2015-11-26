from .usermanager import UserManager
from .tourmanager import TourManager
from .experiencemanager import ExperienceManager
from .registrationmanager import RegistrationManager
from .statisticmanager import StatisticManager

class DBFactory(object):

    def __init__(self):
        self.Tour = TourManager()
        self.Experience = ExperienceManager()
        self.Registration = RegistrationManager()
        self.User = UserManager(self.Experience)
        self.Statistic = StatisticManager(self.Registration, self.Tour)

    # Private member, please use get_instance.
    __instance = None

    @staticmethod
    def get_instance():
        if DBFactory.__instance is None:
            DBFactory.__instance = DBFactory()
            return DBFactory.__instance

        return DBFactory.__instance













