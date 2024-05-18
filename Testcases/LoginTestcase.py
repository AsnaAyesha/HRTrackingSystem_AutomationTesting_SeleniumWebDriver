#  Handle login page using selenium webdriver with python in pyunit testing framework
"""
1)User can check the credentials and verify through enter multiple invalid values
  and generate report if invalid values lead to Dashboard.

2)Confirm once dashboard display after applying valid credentials.
"""

import unittest
import time
import xlrd
import HTMLTestRunner
import datetime

from selenium import webdriver
from ddt import ddt, data, unpack
from Pages.login import LoginPage
from Pages.dashboard import DashboardPage
from selenium.common.exceptions import TimeoutException


def get_data(file_name):
    # Log attempt to open file
    print("Attempting to open file:", file_name)
    rows = []

    try:
        # Open the Excel file
        book = xlrd.open_workbook(file_name)
        sheet = book.sheet_by_index(0)

        # Skip the header row and read the rest
        for i in range(1, sheet.nrows):

            # Read username and password (ignoring first and last columns)
            rows.append(sheet.row_values(i, 1, sheet.ncols - 1))

    except Exception as e:
        print("Error reading Excel file:", e)
        return []

    print("Data successfully loaded from the Excel file.")
    return rows


@ddt
class TestLogin(unittest.TestCase):

    # Screenshot
    chrome_option = webdriver.ChromeOptions()
    # chrome_option.add_argument("--headless")
    chrome_option.add_argument("--start-maximized")

    def setUp(self):
        # Launch the browser
        self.driver = webdriver.Chrome()

        # Maximize the window
        self.driver.maximize_window()

        # Get Url
        self.driver.get("http://localhost/login.do")

        # Synchronize the time
        self.driver.implicitly_wait(10)

    @data(*get_data("TestData/LoginTestData.xlsx"))
    @unpack
    def test_credentials(self, username, password):
        driver = self.driver
        login_page = LoginPage(driver)
        dashboard_page = DashboardPage(driver)

        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.select_checkbox()

        login_page.click_login()

        # Pause time
        time.sleep(2)

        # Check if username or password is empty
        if not username and not password:

            try:
                error_message = login_page.get_error_message()

                self.assertEqual(
                    error_message,
                    "Please enter your username and password.",
                    "Error message for empty username not displayed"
                )

            except TimeoutException:
                self.fail("TimeoutException: Error message not found")

        # Check if username is empty
        elif not username:

            try:
                error_message = login_page.get_error_message()

                self.assertEqual(
                    error_message,
                    "Please enter your username",
                    "Error message for empty username not displayed"
                )

            except TimeoutException:
                self.fail("TimeoutException: Error message not found")

        # Check if password is empty
        elif not password:

            try:
                error_message = login_page.get_error_message()

                self.assertEqual(
                    error_message,
                    "Please enter your password",
                    "Error message for empty password not displayed"
                )

            except TimeoutException:
                self.fail("TimeoutException: Error message not found")
                # print("TimeoutException: Error message not found")

        # Check if username or password are valid
        elif username and password:

            try:
                dashboard_page.is_displayed()

                # Capture image
                element = "loginSuccess"
                date_time = datetime.datetime.now().strftime('%y%m%d_%H%M%S')

                driver.save_screenshot("Screenshot/Login/loginSuccess//" + element + "_" + date_time + ".png")
                print("Dashboard image captured!")

            except:
                # Check if username or password are invalid
                print("Invalid username or password")

                # Capture image
                element = "loginFailure"
                date_time = datetime.datetime.now().strftime('%y%m%d_%H%M%S')

                driver.save_screenshot("Screenshot/Login/LoginFailure//" + element + "_" + date_time + ".png")
                print("Login page image captured!")

    def tearDown(self):
        # Pause time
        time.sleep(2)

        # Close the Browser
        self.driver.close()


if __name__ == '__main__':
    unittest.main(
        testRunner=HTMLTestRunner.HTMLTestRunner(
                        output="C://Users//lenovo//Desktop//python//HumanResourceTrackingSystem//Reports/LoginReport"
                    )
    )


