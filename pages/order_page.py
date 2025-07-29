from .base_page import BasePage
from locators.order_locators import OrderLocators
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from data import FEED_URL
import allure

class OrderPage(BasePage):
    @allure.step('открыть детали последнего заказа')
    def open_last_order_details(self):
        self.click_to_element(OrderLocators.LAST_ORDER)

    @allure.step('получить содержимое деталей заказа')
    def get_order_details_content(self):
        return {
            'id': self.get_text_from_element(OrderLocators.ORDER_ID),
            'status': self.get_text_from_element(OrderLocators.ORDER_STATUS),
            'ingredients': [el.text for el in self.driver.find_elements(*OrderLocators.ORDER_INGREDIENTS_LIST)],
            'price': self.get_text_from_element(OrderLocators.ORDER_TOTAL_PRICE)
        }

    @allure.step("Получить общее количество заказов")
    def get_total_orders_count(self):
        return int(self.get_text_from_element(OrderLocators.TOTAL_ORDERS_COUNTER))

    @allure.step("Получить количество заказов за сегодня")
    def get_today_orders_count(self):
        element = self.find_element_with_wait(OrderLocators.TODAY_COMPLETED_COUNTER)
        return int(element.text.strip())

    @allure.step('открыть страницу ленты заказов')
    def open_feed_page(self):
        self.navigate_to(FEED_URL)
        self.wait_for_element_visible(OrderLocators.FEED_TITLE)

    @allure.step('Перейти в конструктор')
    def navigate_to_constructor(self):
        self.click_to_element(OrderLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Перейти в ленту заказов')
    def navigate_to_feed(self):
        self.wait_for_element_visible(OrderLocators.ORDER_FEED_BUTTON)
        self.click_to_element(OrderLocators.ORDER_FEED_BUTTON)

    @allure.step('создать новый заказ')
    def place_new_order(self):
        self.click_to_element(OrderLocators.PLACE_AN_ORDER)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrderLocators.ORDER_LOADING_MODAL)
        )

    @allure.step('перейти в личный кабинет')
    def navigate_to_account(self):
        self.click_to_element(OrderLocators.ACCOUNT_BUTTON)

    @allure.step('Открыть историю заказов')
    def open_order_history(self):
        self.click_to_element(OrderLocators.ORDER_HISTORY_BUTTON)

    @allure.step('Закрыть детали заказов')
    def close_order_details(self):
        self.click_element_when_ready(OrderLocators.CLOSE_ORDER_DETAILS_BUTTON)

    @allure.step('получить id заказа')
    def get_order_id(self):
        self.find_and_wait_until_text_changes(OrderLocators.ORDER_ID, "9999")
        return self.get_text_from_element(OrderLocators.ORDER_ID)

    @allure.step('Проверить видимость заказа в ленте')
    def is_order_visible_in_feed(self, order_id):
        locator = self.find_and_format_locator(
            (By.XPATH, "//p[contains(text(),'{}')]"),
            order_id
        )
        return self.is_element_visible(locator)

    @allure.step('Проверить статус =Готовится= для заказа id')
    def is_order_in_progress(self, order_id):
        locator = self.find_and_format_locator(
            (By.XPATH, "//p[contains(text(),'{}')]/following::p[contains(text(),'Готовится')]"),
            order_id
        )
        return self.is_element_visible(locator)

    @allure.step('Получить список заказов в работе')
    def get_orders_in_progress(self):
        return [el.text for el in self.driver.find_elements(*OrderLocators.ORDERS_IN_PROGRESS)]

    @allure.step('Получить список заказов в работе в списке выполняемых')
    def is_order_in_progress(self, order_id):
        return order_id in self.get_orders_in_progress()

    @allure.step('Нажать кнопку ленты заказов')
    def click_feed(self):
        self.wait_for_element_visible(OrderLocators.LOGIN_AFTER_LOGOUT_BURGER)
        self.click_element_when_ready(OrderLocators.ORDER_FEED_BUTTON)

    def open_feed_page(self):
        self.navigate_to(FEED_URL)
        self.wait_for_element_visible(OrderLocators.FEED_TITLE)

    @allure.step('Проверить статус выполнения заказа')
    def is_order_in_progress(self, order_number):
        locator = (OrderLocators.ORDER_IN_PROGRESS[0],
                   OrderLocators.ORDER_IN_PROGRESS[1].format(order_number))
        try:
            return self.is_element_visible(locator)
        except:
            return False

    @allure.step('Ожидаем появления заказа  в разделе В работе')
    def wait_for_order_in_progress(self, order_number, timeout=10):
        locator = (OrderLocators.ORDER_IN_PROGRESS[0],
                   OrderLocators.ORDER_IN_PROGRESS[1].format(order_number))
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('получаем id ')
    def get_order_id_from_details(self):
        self.find_and_wait_until_text_changes(OrderLocators.ORDER_ID, "9999")
        return self.get_text_from_element(OrderLocators.ORDER_ID)

    @allure.step('получить общее значение')
    def get_total_orders_count(self):
        return int(self.get_text_from_element(OrderLocators.TOTAL_ORDERS_COUNTER))

    @allure.step('открыть ленту')
    def open_feed_page(self):
        self.driver.get(FEED_URL)
        self.wait_for_element_visible(OrderLocators.FEED_TITLE)

    @allure.step('элемент видимый')
    def is_element_present(self, locator):
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(locator))
            return True
        except:
            return False

    @allure.step("Открыть ленту заказов по прямому URL")
    def open_feed_via_url(self):
        self.driver.get(FEED_URL)
        self.wait_for_page_loaded()
        return self

    @allure.step('номер заказа в работе')
    def is_order_number_in_progress(self, order_number):
        try:
            formatted_id = f"{int(order_number):07d}"
            self.find_and_format_locator(OrderLocators.ORDERS_IN_PROGRESS, formatted_id)
            return True
        except:
            return False

    @allure.step("открыть ленту заказов сегодня")
    def click_feed_today(self):

        self.click_to_element(OrderLocators.ORDER_FEED_BUTTON)

    @allure.step('Получение списка заказов из раздела "В работе"')
    def list_order_id_in_progress(self):
        self.wait_visibility(OrderLocators.ORDERS_IN_PROGRESS)
        return  map(
            lambda li: int(li.text),
            self.find_list(OrderLocators.ORDERS_IN_PROGRESS)
        )

    @allure.step('Ожидает увеличения счетчика Выполнено за сегодня')
    def wait_for_today_counter_increase(self, initial_count, timeout=30):

        WebDriverWait(self.driver, timeout).until(
            lambda d: self.get_today_orders_count() > initial_count
        )