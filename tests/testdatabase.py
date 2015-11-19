import unittest

from app import create_app
from app.db.dbmanager import DBManager
from app.db.models import Experience


class DBManagerTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app('config')
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_get_experiences(self):
        l = [Experience(1, "Könnyű"), Experience(2, "Közepes"),
             Experience(3, "Közepesen nehéz"), Experience(4, "Nehéz")]
        self.assertEquals(DBManager.get_experiences(), l)


if __name__ == '__main__':
    unittest.main()
