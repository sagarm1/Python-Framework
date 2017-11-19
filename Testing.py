import unittest


class Testing (unittest.TestCase):

    def setUp(self):
        print ('COMMON TEST SETUP')
        return

    def tearDown(self):
        print ('COMMON TEST TEARDOWN')