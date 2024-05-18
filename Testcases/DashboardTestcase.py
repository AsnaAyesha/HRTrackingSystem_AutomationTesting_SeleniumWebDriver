# Handle Dashboard Page Using Selenium Webdriver Python in PyUnit Framework

"""
3)Count number of links available throughout the application and also display values
  and verify it.

4)On Dashboard Click on Users
"""

import time
import datetime
import unittest
import HTMLTestRunner
import xlrd

from selenium import webdriver
from Pages.dashboard import DashboardPage
from Pages.login import LoginPage
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
class TestDashboard(unittest.TestCase):

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

        login_page.enter_username(username)
        login_page.enter_password(password)
        login_page.select_checkbox()

        login_page.click_login()

        # Pause Time
        time.sleep(2)

        if username and password:
            dashboard_page.is_displayed()
            dashboard_page.get_link()
            dashboard_page.dashboard_user()

            # Capture image
            element = "button_click"
            date_time = datetime.datetime.now().strftime('%y%m%d_%H%M%S')

            driver.save_screenshot("Screenshot/Dashboard/User//" + element + "_" + date_time + ".png")
            print("Login page image captured!")

        else:
            print("Invalid username or password")

    # def test_user(self):
    #     driver = self.driver
    #     dashboard_page = DashboardPage(driver)

    def tearDown(self):
        # Pause time
        time.sleep(2)

        # Close the Browser
        self.driver.close()

if __name__ == '__main__':
    unittest.main(
        testRunner=HTMLTestRunner.HTMLTestRunner(
            output="C://Users//lenovo//Desktop//python//HumanResourceTrackingSystem//Reports//DashboardReport"
        )
    )