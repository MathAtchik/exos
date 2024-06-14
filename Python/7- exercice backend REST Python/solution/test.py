import unittest
from solution import app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_ask_endpoint(self):
        response = self.app.post('/ask', data="Quelle est la réponse à la grande question de la vie, de l'univers et de tout le reste ?")
        self.assertEqual(response.status_code, 200)
        response_data = response.data.decode('utf-8')
        self.assertIn("La réponse à votre question 'Quelle est la réponse à la grande question de la vie, de l'univers et de tout le reste ?' est 42.", response_data)

if __name__ == '__main__':
    unittest.main()