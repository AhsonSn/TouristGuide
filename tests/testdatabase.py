import unittest

from werkzeug.security import check_password_hash

from app import create_app
from app.db.models import Experience, Tour
from app.db.experiencemanager import ExperienceDAO
from app.db.usermanager import UserDAO
from app.db.tourmanager import TourDAO
from app.db.registrationmanager import RegistrationDAO
from app.db.statisticmanager import StatisticDAO

class DBManagerTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app('config')
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_get_experiences(self):
        l = [Experience(1, "Kezdő"), Experience(2, "Középhaladó"),
             Experience(3, "Haladó"), Experience(4, "Profi")]
        self.assertEquals(ExperienceDAO.get_experiences(), l)

    def test_get_users_by_role(self):
        print(UserDAO.get_user_by_role("Turavezeto"))
        self.assertEquals(True, True)

    def test_update_pwd(self):
        print(UserDAO.update_pwd("test", "test1", "test1"))
        usr = UserDAO.get_user_with_name("test")
        self.assertEquals(True, check_password_hash(usr.password, "test1"))

    def test_update_src(self):
        filename = "kep.jpg"
        from werkzeug.datastructures import FileStorage
        image = FileStorage(filename=filename)
        UserDAO.update_avatar("test", image)
        usr = UserDAO.get_user_with_name("test")
        self.assertEquals(usr.avatar_src, filename)

    def test_update_email(self):
        UserDAO.update_email("test", "mukodik@test.net")
        usr = UserDAO.get_user_with_name("test")
        self.assertEquals(usr.email, "mukodik@test.net")

    def test_update_experience_by_user(self):
        UserDAO.update_experience("test", 4)
        usr = UserDAO.get_user_with_name("test")
        self.assertEquals(usr.experience_id, 4)

    def test_get_list_of_Tour(self):
        l = TourDAO.get_id_list_of_tours_by_date("2015-12-01", "2016-04-01")
        for x in l:
            print(x)
        self.assertEquals(True, True)

    def test_get_registration_by_tour_id(self):
        print(RegistrationDAO.get_registration_count_by_tour_id(1))
        self.assertEquals(True, True)

    def test_ordered_list_from_tour_registrations(self):
        print("Ordered list: ")
        print(StatisticDAO.get_tours("2016-09-01", "2016-10-01"))
        self.assertEquals(True, True)

    def test_ordered_list_from_tour_guide_tours(self):
        print("Statistic2 list: ")
        print(StatisticDAO.get_static_from_tour_guide("2015-09-01", "2016-10-01"))
        self.assertEquals(True, True)

    def test_ordered_list_from_tour_guide_tours_popularity(self):
        print("Statistic3 list: ")
        print(StatisticDAO.get_static_from_tour_guide_popularity("2015-09-01", "2016-10-01"))
        self.assertEquals(True, True)

    def test_delay_tour(self):
        print(TourDAO.delay_tour(1, "2016-09-01 00:00", "2016-10-01 00:00"))
        self.assertEquals(True, True)

    def test_delete_tour(self):
        print(TourDAO.delete_tour(2))
        self.assertEquals(True, True)

    def test_setPrice(self):
        t = Tour("ABC", 3, 2)
        t.id = 1
        t.price = 3000
        l = [t]
        self.assertEquals(TourDAO.set_prices(l), True)


if __name__ == '__main__':
    unittest.main()
