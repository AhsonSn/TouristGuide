import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self):
        from app.db.dbmanager import DBManager
        self.db_manager = DBManager()

    def test_something(self):
        from app.db.models import Experience
        l = [Experience(1, "Könnyű"), Experience(2, "Közepes"), Experience(3, "Közepesen nehéz"), Experience(4, "Nehéz")]
        self.assertEquals(self.db_manager.get_experiences(), l)



if __name__ == '__main__':
    unittest.main()
