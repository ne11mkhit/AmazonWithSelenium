from TestCases.Base_test_file import BaseTestClass
from Common.Variables.variables_file import VariablesClass
from Sources.Pages.Sign_in_page_file import SignInPageClass
from Sources.Pages.Navigation_bar_page_file import NavigationBarClass
from Sources.Pages.Item_page_file import ItemPageClass


class AddToCartTestcase(BaseTestClass):
    def setUp(self):
        # preconditions part
        self.signInPageObj = SignInPageClass(self.driver)
        self.itemObj = NavigationBarClass(self.driver)
        self.itemObj1 = ItemPageClass(self.driver)
        self.itemObj2 = ItemPageClass(self.driver)

    def test_add_item_to_cart(self):
        # Sign-in part
        self.driver.get(VariablesClass.amazonSignInURL)
        self.signInPageObj.fast_sign_in()

        # Search & add to cart part
        self.itemObj.search_the_item()
        self.itemObj.select_item_from_search_results()
        self.itemObj1.change_quantity(2)
        self.itemObj1.click_on_add_to_cart_button()
        self.itemObj1.close_add_to_cart_modal()
        self.itemObj.search_the_item()
        self.itemObj.select_item_from_search_results(5)
        self.itemObj2.click_on_add_to_cart_button()

    def tearDown(self):
        self.driver.close()
