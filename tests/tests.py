import os
import unittest
import xmlrunner

from python_marketman.api import Marketman
from python_marketman.exceptions import MarketmanAuthenticationFailed


class AuthenticationTestCase(unittest.TestCase):

    def test_connect(self):
        with self.assertRaises(MarketmanAuthenticationFailed):
            faulty_credentials = {
                'api_key': 'somekey',
                'api_password': 'somepass'
            }
            Marketman(**faulty_credentials)


if __name__ == '__main__':
    if not os.path.exists('test-results'):
        os.makedirs('test-results')
    with open('test-results/results.xml', 'wb') as output:
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output=output),
            failfast=False, buffer=False, catchbreak=False)
