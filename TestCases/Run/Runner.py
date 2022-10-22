import unittest
from unittest import TestLoader, TextTestRunner, TestSuite
import HtmlTestRunner
from TestCases.Sign_in_test_file import SignInTestcase
from TestCases.Item_search_functionality_test_file import ItemSearchFunctionalityTestCase
from TestCases.Add_item_to_cart_test_file import AddToCartTestcase
from TestCases.Remove_items_from_cart_test_file import RemoveFromCartTestcase
from TestCases.Edit_customers_name_test_file import EditCustomersNameTestCase


class RunnerClass:
    pass


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='TestCases/Run/Reports'))
    loader = TestLoader()

    suite = TestSuite((
        loader.loadTestsFromTestCase(SignInTestcase),
        loader.loadTestsFromTestCase(ItemSearchFunctionalityTestCase),
        loader.loadTestsFromTestCase(AddToCartTestcase),
        loader.loadTestsFromTestCase(RemoveFromCartTestcase),
        loader.loadTestsFromTestCase(EditCustomersNameTestCase)
    ))

    runner = TextTestRunner(verbosity=2)
    runner.run(suite)

