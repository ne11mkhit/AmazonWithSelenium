import names
from Sources.Pages.Base_page_file import BasePageClass
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Common.Variables.variables_file import VariablesClass


class NavigationBarClass(BasePageClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = NavigationBarLocatorsClass

    def go_to_home_page(self):
        amazonLogoButtonElement = self.find_element(self.locators.amazonLogoButtonLocator)
        amazonLogoButtonElement.click()

    def search_the_item(self, search_text=VariablesClass.searchText):
        searchbarFieldElement = self.find_element(self.locators.searchbarFieldLocator)
        searchbarFieldElement.clear()
        searchbarFieldElement.send_keys(search_text)
        searchbarFieldElement.send_keys(Keys.ENTER)

    def select_item_from_search_results(self, n: int = 1):
        foundElements = self.find_elements(self.locators.foundItemsLocator)
        foundItemElement = foundElements[n // 2 + n]
        foundItemElement.click()

    def go_to_shopping_cart_page(self):
        cartButtonElement = self.find_element(self.locators.cartButtonLocator)
        cartButtonElement.click()

    def edit_customers_name(self):
        accountsAndListsElement = self.find_element(self.locators.accountsAndListsLocator)
        accountsAndListsElement.click()
        loginAndSecurityElement = self.find_element(self.locators.loginAndSecurityLocator)
        loginAndSecurityElement.click()
        editNameButtonElement = self.find_element(self.locators.editNameButtonLocator)
        editNameButtonElement.click()
        newNameTextBoxElement = self.find_element(self.locators.newNameTextBoxLocator)
        newNameTextBoxElement.clear()
        newNameTextBoxElement.send_keys(names.get_full_name(gender='female'))
        saveChangesButtonElement = self.find_element(self.locators.saveChangesButtonLocator)
        saveChangesButtonElement.click()


class NavigationBarLocatorsClass:
    amazonLogoButtonLocator = (By.ID, "nav-logo")
    searchbarFieldLocator = (By.ID, "twotabsearchtextbox")
    cartButtonLocator = (By.ID, "nav-cart")
    accountsAndListsLocator = (By.ID, "nav-link-accountList")
    loginAndSecurityLocator = (By.XPATH, "(//h2[@class='a-spacing-none ya-card__heading--rich a-text-normal'])[2]")
    editNameButtonLocator = (By.ID, "auth-cnep-edit-name-button")
    newNameTextBoxLocator = (By.ID, "ap_customer_name")
    saveChangesButtonLocator = (By.ID, "cnep_1C_submit_button")
    foundItemsLocator = (By.CSS_SELECTOR,".a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal")
