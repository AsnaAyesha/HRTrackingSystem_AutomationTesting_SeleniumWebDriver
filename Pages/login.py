# Create a class to reserve all objects from login page

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage():

    def __init__(self, driver):

        self.driver = driver

        self.username_textbox_id = "username"
        self.password_textbox_name = "pwd"
        self.login_button_xpath = "//*[@id='loginButton']/div"
        self.checkbox_id = "keepLoggedInCheckBox"

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def enter_username(self, user_name):

        # Add a element username to assign the data
        username = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, self.username_textbox_id))
        )

        # check whether textbox displayed or not
        username_displayed = username.is_displayed()

        print("-------------------------------------------------")
        print("-------------------------------------------------")
        print("Does username textbox display::", username_displayed)
        print("-------------------------------------------------")

        # verify whether username is displayed in the form
        assert True is username_displayed

        # Check whether textbox enabled or not
        user_enabled = username.is_enabled()

        print("Does username textbox enable::", user_enabled)
        print("-------------------------------------------------")

        # verify whether username is enabled in the form
        assert True is user_enabled

        # Clear the textbox using clear() method
        username.clear()

        # send data in side the textbox
        username.send_keys(user_name)

    def enter_password(self, password):

        # Add an element password to assign the data
        userpassword = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, self.password_textbox_name))
        )

        # check whether textbox displayed or not
        userpassword_displayed = userpassword.is_displayed()

        print("Does password textbox display::", userpassword_displayed)
        print("-------------------------------------------------")

        # verify whether username is displayed in the form
        assert True is userpassword_displayed

        # Check whether textbox enabled or not
        userpassword_enabled = userpassword.is_enabled()

        print("Does user password textbox enable::", userpassword_enabled)
        print("-------------------------------------------------")

        # verify whether userpassword is enabled in the form
        assert True is userpassword_enabled

        # Clear the textbox using clear() method
        userpassword.clear()

        # send data in side the textbox
        userpassword.send_keys(password)

    def select_checkbox(self):
        # Add a element password to assign the data
        checkbox = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, self.checkbox_id))
        )

        # check whether textbox displayed or not
        checkbox_displayed = checkbox.is_displayed()

        print("Does checkbox  display::", checkbox_displayed)
        print("-------------------------------------------------")

        # verify whether checkbox is displayed in the form
        assert True is checkbox_displayed

        # Click on checkbox
        checkbox.click()

    def click_login(self):

        login = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.login_button_xpath))
        )

        # check whether login button displayed or not
        login_display = login.is_displayed()
        print("Does the login  button is displayed::", login_display)
        print("-------------------------------------------------")

        # Verify whether login button displayed or not
        assert True is login_display

        # check whether login button enabled or not
        login_enable = login.is_enabled()
        print("Does the login  button is enabled::", login_enable)
        print("-------------------------------------------------")

        # Verify whether login button enabled or not
        assert True is login_enable

        # Click on login button for redirect to dashboard page
        login.click()

    def get_error_message(self):
        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "errormsg"))
        )

        return error_message.text


