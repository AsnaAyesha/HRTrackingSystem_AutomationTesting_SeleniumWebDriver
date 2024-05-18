# Create a class to reserve all objects from login page

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage():

    def __init__(self,driver):
        self.driver = driver
        self.dashboard_locator_ClassName = "ext-strict"
        self.user_option_xpath = "//*[@id='topnav']/tbody/tr[1]/td[9]/a/div"
        # self.user_button_name = "Users"

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def is_displayed(self):

        dashboard = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, self.dashboard_locator_ClassName))
        )

        # check whether dashboard displayed or not
        dashboard_display = dashboard.is_displayed()

        print("-------------------------------------------------")
        print("-------------------------------------------------")
        print("Does dashboard  display::", dashboard_display)
        print("-------------------------------------------------")

        # verify whether dashboard is displayed in the form
        assert True is dashboard_display

    def get_link(self):
        links = self.driver.find_elements(By.TAG_NAME, "a")

        # Display count of the links in the dashboard
        total_links = len(links)
        print("Total count of the links in the dashboard::", total_links)
        print("-------------------------------------------------")

        # Expected total count of links
        expected_total_links = 32

        # Verify whether count displayed or not
        assert total_links == expected_total_links


        # Display all links in the dashboard
        display_link = []
        print("Links in the dashboard:: \n")

        for link in links:

            # display links in the console
            print(link.text)
            display_link.append(link.text)

        print("-------------------------------------------------")

        return total_links, display_link

    def dashboard_user(self):

        user = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.user_option_xpath))
        )

        # Check whether user button displayed or not
        user_display = user.is_displayed()
        print("User button is displayed::", user_display)
        print("-------------------------------------------------")

        # Check whether user button enable or not
        user_enable = user.is_enabled()
        print("User button is enabled::", user_enable)
        print("-------------------------------------------------")

        # check whether button clickable or not
        user.click()






