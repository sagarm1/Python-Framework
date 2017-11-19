import unittest
from Testing import Testing

class NewClass (Testing):

    # def setUp(self):
    #     print ('setUp in NewCLASS')
    #     return
    #
    # def tearDown(self):
    #     print ('tearDown in NewCLASS')
    #
    # @classmethod
    # def setUpClass(cls):
    #     print ('set up class in NewCLASS')
    #     return
    #
    # @classmethod
    # def tearDownClass(cls):
    #     print ('tearDown class in NewCLASS')
    #     return

    def test_testCase4(self):
        print ('in test case 4 to pass in NewCLASS')
        self.assertEqual(1,1, "Items are equal in test case 1")
        return

    def test_testCase5(self):
        print ('in test case 5 to fail in NewCLASS')
        self.assertEqual(1,2, "Items are not equal in test case 2")

    def test_testCase6(self):
        print ('in test case 6 to pass in NewCLASS')
        self.assertEqual(1,1, "Items are not equal in test case 3")

# def suite():
#     suite = unittest.TestSuite()
#     ##   suite.addTest (simpleTest3("testadd"))
#     suite.addTest (setUpBase("test_testCase3"))
#     # suite.addTest(unittest.makeSuite(setUpBase))
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