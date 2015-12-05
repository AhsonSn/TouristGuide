from .experiencemanager import ExperienceManager
from .messagemanager import MessageManager
from .registrationmanager import RegistrationManager
from .statisticmanager import StatisticManager
from .tourmanager import TourManager
from .usermanager import UserManager


class DBFactory(object):
    def __init__(self):
        self.Tour = TourManager()
        self.Experience = ExperienceManager()
        self.Registration = RegistrationManager()
        self.User = UserManager()
        self.Statistic = StatisticManager(self.Registration, self.Tour, self.User)
        self.Message = MessageManager()

    # Private member, please use get_instance.
    __instance = None

    @staticmethod
    def get_instance():
        if DBFactory.__instance is None:
            DBFactory.__instance = DBFactory()
            return DBFactory.__instance

        return DBFactory.__instance
