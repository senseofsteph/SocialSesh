"""Testing the web app functionality."""

import server
import unittest


class MyAppIntegrationTestCase(unittest.TestCase):
    """Examples of integration tests: testing Flask server."""
    
    def setUp(self):
      """Stuff to do before every test."""

      self.client = server.app.test_client()
      server.app.config['TESTING'] = True

    def tearDown(self):
      """Stuff to do after each test."""

    def test_index(self):
        client = server.app.test_client()
        result = client.get('/')
        self.assertIn(b'<div id="header" class="header">', result.data)

    def test_form(self):
        client = server.app.test_client()
        result = client.get('/form')
        self.assertIn(b'<div id="form-signup" class="form-signup">', result.data)

    def test_login(self):
        client = server.app.test_client()
        result = client.get('/login')
        self.assertIn(b'<div id="form-login" class="form-login">', result.data)
    
    def test_profile(self):
        client = server.app.test_client()
        result = client.get('/profile')
        self.assertIn(b'<div id="profile-header" class="profile-header">', result.data)

    def test_event_details(self):
        client = server.app.test_client()
        result = client.get('/category')
        self.assertIn(b'<div id="event-category" class="event-category">', result.data)
    
    def test_register(self):
        client = server.app.test_client()
        result = client.get('/register')
        self.assertIn(b'<div id="form-register" class="form-register">', result.data)

    def test_confirm(self):
        client = server.app.test_client()
        result = client.get('/confirmation')
        self.assertIn(b'<div id="confirmation-header" class="confirmation-header">', result.data)

    




if __name__ == '__main__':
    unittest.main()