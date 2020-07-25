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

    def test_home_post_route_success(self):
        with app.test_client() as c:
            resp = c.post('/', data={
                'from-code': 'USD',
                'to-code': 'USD',
                'amount': '1'
            })

            self.assertEqual(resp.status_code, 302)
            self.assertIn('http://localhost/rate?converted_amount=US%241.00', resp.location)

    def test_home_post_route_failure(self):
        with app.test_client() as c:
            resp = c.post('/', data={
                'from-code': 'ZZZ',
                'to-code': 'USD',
                'amount': '1'
            }, follow_redirects=True)
            html = resp.get_data(as_text=True)
            
            self.assertEqual(resp.status_code, 200)
            self.assertIn('From code not valid', html)

    def test_rate_get_route(self):
        with app.test_client() as c:
            resp = c.get('/rate?converted_amount=US%241.00')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('US$1.00', html)

    def test_rate_post_route(self):
        with app.test_client() as c:
            resp = c.post('/rate')

            self.assertEqual(resp.status_code, 302)
            self.assertEqual(resp.location, "http://localhost/")
