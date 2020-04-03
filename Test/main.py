import unittest
from ParkingLot import app
from ParkingLot.models import *


class UnitTestCase(unittest.TestCase):

    def setUp(self):
        app.config.update(
            TESTING=True,
        )

        self.client = app.test_client()
        self.runner = app.test_cli_runner()

    def test_app_exist(self):
        self.assertIsNotNone(app)

    def test_app_is_testing(self):
        self.assertTrue(app.config['TESTING'])

    def test_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)

    def test_logout_page(self):
        response = self.client.get('/logout')
        self.assertEqual(response.status_code, 200)


    def test_reg_page(self):
        response = self.client.get('/reg')
        self.assertEqual(response.status_code, 200)
        self.client.post('/reg', data=dict(
            email='xx@xx.com',
            password='xxx'
        ), follow_redirects=True)

    def test_makeRes_page(self):
        response = self.client.get('/makeRes')
        self.assertEqual(response.status_code, 200)

    def test_transaction_page(self):
        response = self.client.get('/transaction')
        self.assertEqual(response.status_code, 200)

    def test_profile_page(self):
        response = self.client.get('/profile?email=test@test.com')
        self.assertEqual(response.status_code, 200)


    def test_admin_page(self):
        response = self.client.get('/admin?email=test@test.com')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/admin')
        self.assertEqual(response.status_code, 200)
        self.client.post('/admin', data=dict(
            email='test@test.com',
            password='123456'
        ), follow_redirects=True)

    def test_admin_login_page(self):
        response = self.client.get('/admin_login')
        self.assertEqual(response.status_code, 200)

    def test_admin_logout_page(self):
        response = self.client.get('/admin_logout')
        self.assertEqual(response.status_code, 200)

    def test_spots_page(self):
        response = self.client.get('/spots')
        self.assertEqual(response.status_code, 200)

    def test_checklogin_page(self):
        self.client.post('/checklogin', data=dict(
            email='test@test.com',
            password='123456'
        ), follow_redirects=True)

        self.client.post('/checklogin', data=dict(
            email='xx@xx.com',
            password='xxx'
        ), follow_redirects=True)



if __name__ == '__main__':
    unittest.main()
