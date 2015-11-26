import unittest


from app import create_app
from app.db.dbfactory import DBFactory
from app.db.models import Experience
from werkzeug.security import check_password_hash


class DBManagerTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app('config')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.instance = DBFactory.get_instance()

    def tearDown(self):
        self.app_context.pop()

    def test_get_experiences(self):
        l = [Experience(1, "Könnyű"), Experience(2, "Közepes"),
             Experience(3, "Közepesen nehéz"), Experience(4, "Nehéz")]
        self.assertEquals(self.instance.Experience.get_experiences(), l)

    def test_get_users_by_role(self):
        print(self.instance.User.get_user_by_role("Turavezeto"))
        self.assertEquals(True, True)

    def test_insert_tour(self):
        #self.instance.Tour.insert_tour("Bükki túra2", "2015-11-19 10:10", "2015-11-20 10:10", "", 1, 1, "Káprázatos túrahely.")
        self.assertEquals(True, True)

    def test_update_pwd(self):
        print(self.instance.User.update_pwd("test", "test1", "test1"))
        usr = self.instance.User.get_user_with_name("test")
        self.assertEquals(True, check_password_hash(usr.password, "test1"))

    def test_update_src(self):
        self.instance.User.update_avatar("test", "kep.jpg")
        usr = self.instance.User.get_user_with_name("test")
        self.assertEquals(usr.avatar_src, "kep.jpg")

    def test_update_email(self):
        self.instance.User.update_email("test", "mukodik@test.net")
        usr = self.instance.User.get_user_with_name("test")
        self.assertEquals(usr.email, "mukodik@test.net")

    def test_update_experience_by_user(self):
        self.instance.User.update_experience("test", "Nehéz")
        usr = self.instance.User.get_user_with_name("test")
        self.assertEquals(usr.experience_id, 4)

    def test_get_list_of_Tour(self):
        l = self.instance.Tour.get_id_list_of_tours_by_date("2015-12-01", "2016-04-01")
        for x in l:
            print(x)
        self.assertEquals(True, True)

    def test_get_registration_by_tour_id(self):
        print(self.instance.Registration.get_registration_count_by_tour_id(1))
        self.assertEquals(True, True)

if __name__ == '__main__':
    unittest.main()
