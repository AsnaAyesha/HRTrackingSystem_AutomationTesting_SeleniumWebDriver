# Create a class to deserve all objects in the user page

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UserPage():

    def __init__(self, driver):

        self.driver = driver
        self.newUser_button_id = "ext-comp-1003"
        self.newUser_form_className = "innerContent"
        self.createUser_button_id = "userDataLightBox_commitBtn"

    def newUser(self):
        newUser = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, self.newUser_button_id))
        )

        # check whether new user button displayed or not
        newUser_displayed = newUser.is_displayed()
        print("-------------------------------------------------")
        print("-------------------------------------------------")

        print("Does new user button displayed or not::", newUser_displayed)
        print("-------------------------------------------------")

        # Verify whether new user button displayed or not
        assert True is newUser_displayed

        # Check whether new user button enabled or not
        newUser_enabled = newUser.is_enabled()
        print("Does new user button enabled or not::", newUser_enabled)
        print("-------------------------------------------------")

        # verify whether new user button enabled or not
        assert True is newUser_enabled

        # Check whether newbutton clickable or not
        newUser.click()

    def form(self):

        newUserForm = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, self.newUser_form_className))
        )

        # check whether user form displayed or not
        newUserForm_displayed = newUserForm.is_displayed()
        print("Does user form displayed or not::", newUserForm_displayed)
        print("-------------------------------------------------")

        # Verify whether user form displayed or not
        assert True is newUserForm_displayed

    def click_create(self):

        createButton = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "userDataLightBox_commitBtn"))
        )

        createButton.click()




