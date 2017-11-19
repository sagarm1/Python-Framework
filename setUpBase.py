import unittest

from Testing import Testing


class setUpBase (Testing):

    # def setUp(self):
    #     print ('setUp in SETUPBASE')
    #     return
    #
    # def tearDown(self):
    #     print ('tearDown in SETUPBASE')
    #
    # @classmethod
    # def setUpClass(cls):
    #     print ('set up class in SETUPBASE')
    #     return
    #
    # @classmethod
    # def tearDownClass(cls):
    #     print ('tearDown class in SETUPBASE')
    #     return

    def test_testCase1(self):
        print ('in test case 1 to pass in SETUPBASE')
        self.assertEqual(1,1, "Items are equal in test case 1")
        return

    def test_testCase2(self):
        print ('in test case 2 to fail in SETUPBASE')
        self.assertEqual(1,2, "Items are not equal in test case 2")

    def test_testCase3(self):
        print ('in test case 3 to pass in SETUPBASE')
        self.assertEqual(1,1, "Items are not equal in test case 3")

# def suite():
#     suite = unittest.TestSuite()
#     ##   suite.addTest (simpleTest3("testadd"))
#     # suite.addTest (setUpBase("test_testCase3"))
#     suite.addTest(unittest.makeSuite(setUpBase))
#     return suite
#
#
# if __name__ == '__main__':
#     runner = unittest.TextTestRunner()
#     test_suite = suite()
#     runner.run(test_suite)


# if __name__ == '__main__':
#     suiteTest = unittest.TestSuite()
#     suiteTest.adddTests(setUpBase)
#     runner = unittest.TextTestRunner()
#     runner.run(suiteTest)