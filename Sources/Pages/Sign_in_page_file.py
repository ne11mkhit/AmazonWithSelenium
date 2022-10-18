import time
from selenium.webdriver.common.by import By
from Sources.Pages.Base_page_file import BasePageClass
from Common.Variables.variables_file import VariablesClass


class SignInPageClass(BasePageClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = SignInPageLocators

    def fill_username_field(self, username_=VariablesClass.get_username()):
        emailFieldElement = self.find_element(self.locators.emailFieldLocator)
        emailFieldElement.clear()
        emailFieldElement.send_keys(username_)

    def click_continue(self):
        continueButtonElement = self.find_element(self.locators.continueButtonLocator)
        continueButtonElement.click()

    def fill_password_field(self, password_=VariablesClass.get_password()):
        passwordFieldElement = self.find_element(self.locators.passwordFieldLocator)
        passwordFieldElement.send_keys(password_)

    def click_keep_me_signed_in(self):
        rememberMeCheckboxElement = self.find_element(self.locators.rememberMeCheckboxLocator)
        rememberMeCheckboxElement.click()

    def click_sign_in_button(self):
        signInButtonElement = self.find_element(self.locators.signInButtonLocator)
        signInButtonElement.click()

    def fast_sign_in(self, username=VariablesClass.get_username(), password=VariablesClass.get_password()):
        """Opens Amazon.com sign in page and singes in.
            We can specify a username and password, otherwise the default values will be used."""
        self.driver.get(VariablesClass.amazonSignInURL)
        # username
        self.fill_username_field(username)
        time.sleep(2)  # added to not get robot check
        self.click_continue()
        # password
        self.fill_password_field(password)
        time.sleep(2)  # added to not get robot check
        self.click_sign_in_button()


class SignInPageLocators:
    emailFieldLocator = (By.NAME, "email")
    continueButtonLocator = (By.ID, "continue")
    passwordFieldLocator = (By.ID, "ap_password")
    rememberMeCheckboxLocator = (By.NAME, "rememberMe")
    signInButtonLocator = (By.ID, "signInSubmit")

