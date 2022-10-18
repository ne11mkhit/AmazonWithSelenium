import time
from TestCases.Base_test_file import BaseTestClass
from Sources.Pages.Sign_in_page_file import SignInPageClass
from Common.Variables.variables_file import VariablesClass


class SignInTestcase(BaseTestClass):
    def setUp(self):
        # preconditions part
        self.signInPageObj = SignInPageClass(self.driver)

    def test_amazon_login(self):
        self.driver.get(VariablesClass.amazonSignInURL)
        self.signInPageObj.fill_username_field()
        time.sleep(2)
        self.signInPageObj.click_continue()
        self.signInPageObj.fill_password_field()
        time.sleep(2)
        self.signInPageObj.click_keep_me_signed_in()
        time.sleep(1)
        self.signInPageObj.click_sign_in_button()

    def tearDown(self):
        self.driver.close()