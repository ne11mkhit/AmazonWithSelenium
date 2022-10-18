from TestCases.Base_test_file import BaseTestClass
from Sources.Pages.Sign_in_page_file import SignInPageClass
from Common.Variables.variables_file import VariablesClass
from Sources.Pages.Navigation_bar_page_file import NavigationBarClass


class EditCustomersNameTestCase(BaseTestClass):
    def setUp(self):
        # preconditions part
        self.signInPageObj = SignInPageClass(self.driver)
        self.navigationBarObj = NavigationBarClass(self.driver)

    def test_username_edit(self):
        self.driver.get(VariablesClass.amazonSignInURL)

        # Sign-in part
        self.signInPageObj.fast_sign_in()

        # Name edit part
        self.navigationBarObj.edit_customers_name()

    def tearDown(self):
        self.driver.close()
