import unittest

from app import create_app
from app.basic.email import Email


class EmailTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app('config')
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_sendEmail(self):
        email = ['firstvan@live.com']
        subject = 'Test message'
        m = "Hello! \n This is a test mesage from TouristGuideApp."
        self.assertEqual(Email.send_email(email, subject, m), True)

if __name__ == '__main__':
    unittest.main()
