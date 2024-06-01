# tests/test_api.py

import unittest
import requests

class TestAPI(unittest.TestCase):
    def test_get_user(self):
        response = requests.get('http://api.example.com/users/1')
        self.assertEqual(response.status_code, 200)
        user_data = response.json()
        self.assertEqual(user_data['id'], 1)
        self.assertEqual(user_data['name'], 'John Doe')

if __name__ == '__main__':
    unittest.main()
