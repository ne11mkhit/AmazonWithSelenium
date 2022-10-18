import time
from Sources.Pages.Amazon_shopping_cart_page_file import AmazonShoppingCartClass
from Sources.Pages.Navigation_bar_page_file import NavigationBarClass
from Sources.Pages.Sign_in_page_file import SignInPageClass
from TestCases.Base_test_file import BaseTestClass
from Common.Variables.variables_file import VariablesClass


class RemoveFromCartTestcase(BaseTestClass):
    def setUp(self):
        # preconditions part
        self.signInPageObj = SignInPageClass(self.driver)
        self.navigationBarObj = NavigationBarClass(self.driver)
        self.cartObj = AmazonShoppingCartClass(self.driver)

    def test_remove_items_from_cart(self):
        # Sign-in part
        self.driver.get(VariablesClass.amazonSignInURL)
        self.signInPageObj.fast_sign_in()

        # Product removing part
        self.navigationBarObj.go_to_shopping_cart_page()
        self.cartObj.remove_item_from_cart()  # removes first product from the cart
        time.sleep(2)
        self.cartObj.remove_all_items_from_cart()  # removes ALL products from the cart

    def tearDown(self):
        self.driver.close()
