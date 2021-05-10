"""Testing the web app functionality."""

import server
import unittest


class MyAppIntegrationTestCase(unittest.TestCase):
    """Examples of integration tests: testing Flask server."""
    
    def setUp(self):
      """Stuff to do before every test."""

      self.client = app.test_client()
      server.app.config['TESTING'] = True

    def tearDown(self):
      """Stuff to do after each test."""

    def test_index(self):
        client = server.app.test_client()
        result = client.get('/')
        self.assertIn(b'<div id="header" class="header">', result.data)


if __name__ == '__main__':
    unittest.main()