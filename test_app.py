from unittest import TestCase
from flask import jsonify
from app import app

# Make Flask errors be real errors, not HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class AppViewsTests(TestCase):

    def test_home_get_route(self):
        with app.test_client() as c:
            resp = c.get('/')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn(
                '<form class="mb-3" id="currency-form" action="/" method="POST">', html)

    def test_home_post_route(self):
        with app.test_client() as c:
            resp = c.post('/', data={
                'from-code': 'USD',
                'to-code': 'EUR',
                'amount': '1'
            })
            self.assertEqual(resp.status_code, 302)
            self.assertIn('http://localhost/rate?exchange_rate', resp.location)

    def test_rate_get_route(self):
        with app.test_client() as c:
            resp = c.get('/rate')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('The result is:', html)

    def test_rate_post_route(self):
        with app.test_client() as c:
            resp = c.post('/rate')

            self.assertEqual(resp.status_code, 302)
            self.assertEqual(resp.location, "http://localhost/")
