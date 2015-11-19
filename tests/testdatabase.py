import unittest

from app.db.dbmanager import DBManager


class DBManagerTest(unittest.TestCase):
    def test_get_experiences(self):
        from app.db.models import Experience
        l = [Experience(1, "Könnyű"), Experience(2, "Közepes"),
             Experience(3, "Közepesen nehéz"), Experience(4, "Nehéz")]
        self.assertEquals(DBManager.get_experiences(), l)


if __name__ == '__main__':
    unittest.main()
