import unittest
from setUpBase import setUpBase as Test1
from NewCLASS import NewClass as Test2

testList = [Test1, Test2]
testLoad = unittest.TestLoader()

TestList = []
for testCase in testList:
    testSuite = testLoad.loadTestsFromTestCase(testCase)
    TestList.append(testSuite)

newSuite = unittest.TestSuite(TestList)
runner = unittest.TextTestRunner()
runner.run(newSuite)