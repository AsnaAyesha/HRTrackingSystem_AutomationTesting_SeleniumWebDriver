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
        self.firstName_textbox_id = "userDataLightBox_firstNameField"
        self.middleName_textbox_id = "userDataLightBox_middleNameField"
        self.lastName_textbox_id = "userDataLightBox_lastNameField"
        self.email_textbox_id = "userDataLightBox_emailField"
        self.username_textbox_id = "userDataLightBox_usernameField"
        self.password_textbox_id = "userDataLightBox_passwordField"
        self.reenterpassword_textbox_id = "userDataLightBox_passwordCopyField"
        self.hire_date_id = "ext-comp-1128"
        self.hiredDatePicker_id = "ext-gen116"
        self.hire_date_forword_id = "ext-gen118"
        self.hire_date_actual_xpath = "/html/body/div[4]/ul/li/div/table/tbody/tr[1]/td[2]/table/tbody/tr/td[2]/em/button"
        self.hire_date_expected_xpath = "/html/body/div[4]/ul/li/div/table/tbody/tr[1]/td[2]/table/tbody/tr/td[2]/em/button"
        self.hired_expected_date_xpath = "/html/body/div[4]/ul/li/div/table/tbody/tr[2]/td/table/tbody/tr[5]/td[4]/a/em/span"
        self.release_date_id = "ext-gen73"
        self.releaseDatePicker_id = "ext-gen246"
        self.release_ok_button_id = "ext-gen152"
        self.release_date_xpath = "/html/body/div[4]/ul/li/div/table/tbody/tr[2]/td/table/tbody/tr[5]/td[6]/a/em/span"

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

    def newUserEnable(self):

        newUser = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, self.newUser_button_id))
        )

        # Check whether new user button enabled or not
        newUser_enabled = newUser.is_enabled()
        print("Does new user button enabled or not::", newUser_enabled)
        print("-------------------------------------------------")

        # verify whether new user button enabled or not
        assert True is newUser_enabled

        # Check whether newbutton clickable or not
        newUser.click()

        return newUser_enabled

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

    def firstName(self, fname):

        fname_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, self.firstName_textbox_id))
        )

        # check whether first name textbox displayed or not
        fname_displayed = fname_input.is_displayed()
        print("Does first name textbox displayed or not::", fname_displayed)
        print("-------------------------------------------------")

        # verify whether first name textbox displayed or not
        assert fname_displayed is True

        # check whether first name textbox enabled  or not
        fname_enabled = fname_input.is_enabled()
        print("Does first name textbox enabled or not::", fname_enabled)
        print("-------------------------------------------------")

        # verify whether first name textbox enabled  or not
        assert fname_enabled is True

        # Clear the middle name textbox
        fname_input.clear()

        # Send the middle name
        fname_input.send_keys(fname)

    def middleName(self, mname):

        mname_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, self.middleName_textbox_id))
        )

        # check whether middle name textbox displayed or not
        mname_displayed = mname_input.is_displayed()
        print("Does middle name textbox displayed or not::", mname_displayed)
        print("-------------------------------------------------")

        # verify whether middle name textbox displayed or not
        assert mname_displayed is True

        # check whether middle name textbox enabled or not
        mname_enabled = mname_input.is_enabled()
        print("Does middle name textbox enabled or not::", mname_enabled)
        print("-------------------------------------------------")

        # verify whether emailtextbox enabled  or not
        assert mname_enabled is True

        # Clear the email textbox
        mname_input.clear()

        # Send the email
        mname_input.send_keys(mname)

    def lastName(self, lname):

        lname_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, self.lastName_textbox_id))
        )

        # check whether last name textbox displayed or not
        lname_displayed = lname_input.is_displayed()
        print("Does last name textbox displayed or not::", lname_displayed)
        print("-------------------------------------------------")

        # verify whether last name textbox displayed or not
        assert lname_displayed is True

        # check whether last name textbox enabled or not
        lname_enabled = lname_input.is_enabled()
        print("Does last name textbox enabled or not::", lname_enabled)
        print("-------------------------------------------------")

        # verify whether last name textbox enabled  or not
        assert lname_enabled is True

        # Clear the last name textbox
        lname_input.clear()

        # Send the last name
        lname_input.send_keys(lname)

    def emailId(self, email):

        email_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, self.email_textbox_id))
        )

        # check whether email textbox displayed or not
        email_displayed = email_input.is_displayed()
        print("Does email textbox displayed or not::", email_displayed)
        print("-------------------------------------------------")

        # verify whether email textbox displayed or not
        assert email_displayed is True

        # check whether email textbox enabled or not
        email_enabled = email_input.is_enabled()
        print("Does email name textbox enabled or not::", email_enabled)
        print("-------------------------------------------------")

        # verify whether email textbox enabled  or not
        assert email_enabled is True

        # Clear the email textbox
        email_input.clear()

        # Send the email
        email_input.send_keys(email)

    def userName(self, uname):

        uname_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, self.username_textbox_id))
        )

        # check whether username textbox displayed or not
        uname_displayed = uname_input.is_displayed()
        print("Does username textbox displayed or not::", uname_displayed)
        print("-------------------------------------------------")

        # verify whether username textbox displayed or not
        assert uname_displayed is True

        # check whether username textbox enabled or not
        uname_enabled = uname_input.is_enabled()
        print("Does username textbox enabled or not::", uname_enabled)
        print("-------------------------------------------------")

        # verify whether username textbox enabled  or not
        assert uname_enabled is True

        # Clear the username textbox
        uname_input.clear()

        # Send the username
        uname_input.send_keys(uname)

    def userPassword(self, password):

        password_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, self.password_textbox_id))
        )

        # check whether password textbox displayed or not
        password_displayed = password_input.is_displayed()
        print("Does password textbox displayed or not::", password_displayed)
        print("-------------------------------------------------")

        # verify whether password textbox displayed or not
        assert password_displayed is True

        # check whether password textbox enabled or not
        password_enabled = password_input.is_enabled()
        print("Does password textbox enabled or not::", password_enabled)
        print("-------------------------------------------------")

        # verify whether password textbox enabled  or not
        assert password_enabled is True

        # Clear the password textbox
        password_input.clear()

        # Send the password
        password_input.send_keys(password)

    def userReenterPassword(self, repassword):

        repassword_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, self.reenterpassword_textbox_id))
        )

        # check whether re-re enter password textbox displayed or not
        password_displayed = repassword_input.is_displayed()
        print("Does re-enter password textbox displayed or not::", password_displayed)
        print("-------------------------------------------------")

        # verify whether re-enter password textbox displayed or not
        assert password_displayed is True

        # check whether re-enter password textbox enabled or not
        password_enabled = repassword_input.is_enabled()
        print("Does re-enter password textbox enabled or not::", password_enabled)
        print("-------------------------------------------------")

        # verify whether re-enter password textbox enabled  or not
        assert password_enabled is True

        # Clear the re-enter password textbox
        repassword_input.clear()

        # Send the re-enter password
        repassword_input.send_keys(repassword)

    def dateHired(self):
        hiredate = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, self.hire_date_id))
        )

        # check whether calendar textbox is displayed or not
        calendar_displayed = hiredate.is_displayed()

        print("Does the page have a calendar display?::", calendar_displayed)
        print("--------------------------------------------------------------")

        # check whether calendar textbox is enabled or not
        calendar_enabled = hiredate.is_enabled()

        print("Does the page have a calendar enabled?::", calendar_enabled)
        print("--------------------------------------------------------------")

        # Click on the textbox of the calendar
        hiredate.click()

        # Check whether date picker visible or not
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, self.hiredDatePicker_id))
            )
            print("Date Picker Visible in the page")


        except:
            print("Date Picker does not Visible in the page")

        print("--------------------------------------------------------------")

        try:

            prev_option = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.ID, self.hiredDatePicker_id))
            )

            # check whether calendar textbox is displayed or not
            prev_option_displayed = prev_option.is_displayed()

            print("Does the prevoius icon display?::", prev_option_displayed)
            print("--------------------------------------------------------------")

            # check whether calendar textbox is enabled or not
            prev_option_enabled = prev_option.is_enabled()

            print("Does the prevoius icon enabled?::", prev_option_enabled)
            print("--------------------------------------------------------------")

            # actual month and year
            actual_month_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.hire_date_expected_xpath))
            )
            actual_month = actual_month_element.text
            print("Display actual month and year::", actual_month)
            print("--------------------------------------------------------------")

            expected_date = "25 January 2024"

            if actual_month == expected_date:
                print(" Both actual and expected months are same")

            else:

                # Click on the textbox of the calendar
                for i in range(0,5):

                    prev_option.click()

                # Expected month and year
                expected_month_element = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, self.hire_date_expected_xpath))
                )

                expected_month = expected_month_element.text
                print("Display expected month and year::", expected_month)
                print("--------------------------------------------------------------")

            # Select date 25 from the january calendar
            select_date = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.hired_expected_date_xpath))
            )
            print("Expected Date::", select_date.text)
            print("--------------------------------------------------------------")

            # click on selected date
            select_date.click()

            expected_date_month_year = select_date.text + " " + expected_month
            print("Expected date/month/year::", expected_date_month_year)
            print("--------------------------------------------------------------")

        except:

            print("Previous icon does not working properly")
            print("--------------------------------------------------------------")

    def dateRelease(self):
        release_date = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, self.release_date_id))
        )

        # check whether calendar textbox is displayed or not
        calendar2_displayed = release_date.is_displayed()

        print("Does the page have a calendar display?::", calendar2_displayed)
        print("--------------------------------------------------------------")

        # check whether calendar textbox is enabled or not
        calendar2_enabled = release_date.is_enabled()

        print("Does the page have a calendar enabled?::", calendar2_enabled)
        print("--------------------------------------------------------------")

        # Click on the textbox of the calendar
        release_date.click()


        # click on today date
        selected_release_date = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.release_date_xpath))
        )

        # Click on release date
        selected_release_date.click()

        print("Release Date::", selected_release_date.text)
        print("--------------------------------------------------------------")


    def click_create(self):

        createButton = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "userDataLightBox_commitBtn"))
        )

        createButton.click()

