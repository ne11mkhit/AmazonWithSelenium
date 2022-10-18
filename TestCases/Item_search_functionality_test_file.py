from TestCases.Base_test_file import BaseTestClass
from Common.Variables.variables_file import VariablesClass
from Sources.Pages.Sign_in_page_file import SignInPageClass
from Sources.Pages.Navigation_bar_page_file import NavigationBarClass
from Sources.Pages.Item_page_file import ItemPageClass


class ItemSearchFunctionalityTestCase(BaseTestClass):
    def setUp(self):
        # preconditions part
        self.itemObj = NavigationBarClass(self.driver)

    def test_item_search_functionality(self):
        # Search & add to cart part
        self.driver.get("https://www.amazon.com")
        self.assertIn("Amazon.com. Spend less. Smile more.", self.driver.title)
        self.itemObj.search_the_item()
        self.itemObj.select_item_from_search_results()

    def tearDown(self):
        self.driver.close()
