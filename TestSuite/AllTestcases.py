# Run all testcases using test suites

import unittest
from Testcases.LoginTestcase import TestLogin
from Testcases.DashboardTestcase import TestDashboard
from Testcases.UserTestcase import TestUser


def suite():
    test_suite = unittest.TestSuite()

    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestLogin))
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestDashboard))
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestUser))

    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
