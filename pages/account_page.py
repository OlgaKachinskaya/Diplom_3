from .base_page import BasePage
from locators.account_page_locators import AccountPageLocators
from data import LOGIN_URL


class AccountPage(BasePage):
    def is_logout_button_visible(self):
        return self.is_element_visible(AccountPageLocators.LOGOUT_BUTTON)

    def is_login_button_visible_after_logout(self):
        return self.is_element_visible(AccountPageLocators.LOGIN_AFTER_LOGOUT_BURGER)

    def open_login_page(self):
        self.driver.get(LOGIN_URL)

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()


    def click_account_button(self):
        self.click_to_element(AccountPageLocators.ACCOUNT_BUTTON)

    def enter_email(self, email):
        email_input = self.driver.find_element(*AccountPageLocators.EMAIL_INPUT)
        email_input.clear()
        email_input.send_keys(email)

    def enter_password(self, password):
        password_input = self.driver.find_element(*AccountPageLocators.PASSWORD_INPUT)
        password_input.clear()
        password_input.send_keys(password)

    def click_login(self):
        self.click_to_element(AccountPageLocators.LOGIN_BUTTON)

    def is_profile_button_present(self):
        return self.is_element_present(AccountPageLocators.PROFILE_BUTTON)

    def click_order_history(self):
        self.click_to_element(AccountPageLocators.ORDER_HISTORY_BUTTON)

    def logout(self):
        self.click_to_element(AccountPageLocators.LOGOUT_BUTTON)

    def get_completed_orders_count(self):
        return len(self.driver.find_elements(*AccountPageLocators.ORDER_COMPLETED))

    def update_profile_info(self, name=None, email=None):
        if name:
            name_input = self.driver.find_element(*AccountPageLocators.PROFILE_NAME_INPUT)
            name_input.clear()
            name_input.send_keys(name)
        if email:
            email_input = self.driver.find_element(*AccountPageLocators.PROFILE_EMAIL_INPUT)
            email_input.clear()
            email_input.send_keys(email)
        self.click_to_element(AccountPageLocators.SAVE_BUTTON)