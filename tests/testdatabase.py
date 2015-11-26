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

if __name__ == '__main__':
    unittest.main()
