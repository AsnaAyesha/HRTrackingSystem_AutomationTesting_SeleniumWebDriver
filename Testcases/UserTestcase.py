#
"""
4)On Dashboard Click on Users,check whether create new user button is enabled or not.

5)if enable then click on it.

6)User form should be displayed, without filling form click on Submit button
 or Create New User button. and check whether error msg displayed or not and verify it.
"""



import time
import datetime
import unittest
import HTMLTestRunner
import xlrd

from selenium import webdriver
from Pages.dashboard import DashboardPage
from Pages.login import LoginPage
from Pages.user import UserPage
from ddt import ddt, data, unpack

def get_data(file_name):
    # Log attempt to open file
    print("Attempting to open file:", file_name)
    rows = []
    try:
        # Open the Excel file
        book = xlrd.open_workbook(file_name)
        sheet = book.sheet_by_index(1)

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
class TestUser(unittest.TestCase):

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
    def test_dashboardLinks(self, username, password):

        driver = self.driver
        login_page = LoginPage(driver)
        dashboard_page = DashboardPage(driver)
        user_page = UserPage(driver)

        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.select_checkbox()

        login_page.click_login()

        # Pause Time
        time.sleep(2)

        try:

            if username and password:
                dashboard_page.is_displayed()
                dashboard_page.dashboard_user()
                user_page.newUser()

                user_page.form()
                user_page.click_create()

                # Pause time
                time.sleep(2)

                # Capture image
                element = "Form"
                date_time = datetime.datetime.now().strftime('%y%m%d_%H%M%S')

                driver.save_screenshot("Screenshot/User//" + element + "_" + date_time + ".png")
                print("Login page image captured!")

            else:
                print("Invalid username or password")

        except TimeoutError:
            self.fail("TimeoutException: Error message not found")

    def tearDown(self):
        # Pause time
        time.sleep(2)

        # Close the Browser
        self.driver.close()


if __name__ == '__main__':
    unittest.main(
        testRunner=HTMLTestRunner.HTMLTestRunner(
            output="C://Users//lenovo//Desktop//python//HumanResourceTrackingSystem//Reports//UserReport"
        )
    )
