from .base_page import BasePage
from locators.account_page_locators import AccountPageLocators
from data import LOGIN_URL
import allure

class AccountPage(BasePage):
    @allure.step('Проверить видимость кнопки выхода')
    def is_logout_button_visible(self):
        return self.is_element_visible(AccountPageLocators.LOGOUT_BUTTON)

    @allure.step('Проверить видимость кнопки входа после выхода')
    def is_login_button_visible_after_logout(self):
        return self.is_element_visible(AccountPageLocators.LOGIN_AFTER_LOGOUT_BURGER)

    @allure.step('Открыть страницу входа')
    def open_login_page(self):
        self.navigate_to(LOGIN_URL)

    @allure.step('Выполнить вход')
    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    @allure.step('Нажать кнопку "Личный кабинет"')
    def click_account_button(self):
        self.click_to_element(AccountPageLocators.ACCOUNT_BUTTON)

    @allure.step('Ввести email')
    def enter_email(self, email):
        self.add_text_to_element(AccountPageLocators.EMAIL_INPUT, email)

    @allure.step('Ввести пароль')
    def enter_password(self, password):
        self.add_text_to_element(AccountPageLocators.PASSWORD_INPUT, password)

    @allure.step('Нажать кнопку "Войти')
    def click_login(self):
        self.click_to_element(AccountPageLocators.LOGIN_BUTTON)

    @allure.step('Проверить наличие кнопки профиля')
    def is_profile_button_present(self):
        return self.is_element_present(AccountPageLocators.PROFILE_BUTTON)

    @allure.step('Нажать кнопку "История заказов"')
    def click_order_history(self):
        self.click_to_element(AccountPageLocators.ORDER_HISTORY_BUTTON)

    @allure.step('Разлогиниться')
    def logout(self):
        self.click_to_element(AccountPageLocators.LOGOUT_BUTTON)

    @allure.step('Получить количество завершенных заказов')
    def get_completed_orders_count(self):
        return len(self.find_list(AccountPageLocators.ORDER_COMPLETED))

    @allure.step('обновить данные профиля')
    def update_profile_info(self, name=None, email=None):
        if name:
            self.add_text_to_element(AccountPageLocators.PROFILE_NAME_INPUT, name)
        if email:
            self.add_text_to_element(AccountPageLocators.PROFILE_EMAIL_INPUT, email)
        self.click_to_element(AccountPageLocators.SAVE_BUTTON)