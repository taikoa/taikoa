import unittest

import taikoa


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        taikoa.app.config['TESTING'] = True
        self.app = taikoa.app.test_client()

    def tearDown(self):
        pass

    def test_contact(self):
        rv = self.app.post('/contact_form', data={'subject': 'Hello', 'company': 'Raro',
                                                  'message': 'Message', 'email': 'hello@taikoa.net'
                                                  }, follow_redirects=True)
        assert 'Message sent correctly, Thank you.' in rv.data

    def test_contact_error(self):
        rv = self.app.post('/contact_form', data={'subject': 'Hello', 'company': 'Raro',
                                                  'message': 'Message', 'email': 'hello@.net'
                                                  }, follow_redirects=True)
        assert 'Form error, please fix the error in the email' in rv.data


if __name__ == '__main__':
    unittest.main()
