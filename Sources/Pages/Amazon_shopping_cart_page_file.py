from Sources.Pages.Base_page_file import BasePageClass
from selenium.webdriver.common.by import By


class AmazonShoppingCartClass(BasePageClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = AmazonShoppingCartLocatorsClass()

    def remove_item_from_cart(self):
        deleteButtonElement = self.find_element(self.locators.deleteFirstItemButtonLocator)
        deleteButtonElement.click()

    def remove_all_items_from_cart(self):
        productQuantityElement = self.find_element(self.locators.productQuantityElementLocator)
        productQuantity = int(productQuantityElement.text)
        deleteButtonElement = self.find_element(self.locators.deleteFirstItemButtonLocator)
        while productQuantity != 0:
            deleteButtonElement.click()


class AmazonShoppingCartLocatorsClass:
    deleteFirstItemButtonLocator = (By.XPATH, "//input[@value='Delete']")
    productQuantityElementLocator = (By.ID, "nav-cart-count")
