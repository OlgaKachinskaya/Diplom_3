from .base_page import BasePage
from locators.order_locators import OrderLocators
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class OrderPage(BasePage):
    def open_last_order_details(self):
        self.click_to_element(OrderLocators.LAST_ORDER)

    def get_order_details_content(self):
        return {
            'id': self.get_text_from_element(OrderLocators.ORDER_ID),
            'status': self.get_text_from_element(OrderLocators.ORDER_STATUS),
            'ingredients': [el.text for el in self.driver.find_elements(*OrderLocators.ORDER_INGREDIENTS_LIST)],
            'price': self.get_text_from_element(OrderLocators.ORDER_TOTAL_PRICE)
        }

    def get_total_orders_count(self):
        return int(self.get_text_from_element(OrderLocators.TOTAL_ORDERS_COUNTER))

    def get_today_orders_count(self):
        return int(self.get_text_from_element(OrderLocators.TODAY_COMPLETED_COUNTER))

    def open_feed_page(self):
        self.navigate_to(FEED_URL)

    def navigate_to_constructor(self):
        self.click_to_element(OrderLocators.CONSTRUCTOR_BUTTON)

    def navigate_to_feed(self):
        self.wait_for_element_visible(OrderLocators.ORDER_FEED_BUTTON)
        self.click_to_element(OrderLocators.ORDER_FEED_BUTTON)

    def place_new_order(self):
        self.click_to_element(OrderLocators.PLACE_AN_ORDER)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrderLocators.ORDER_LOADING_MODAL)
        )

    def navigate_to_account(self):
        self.click_to_element(OrderLocators.ACCOUNT_BUTTON)

    def open_order_history(self):
        self.click_to_element(OrderLocators.ORDER_HISTORY_BUTTON)

    def close_order_details(self):
        self.click_to_element(OrderLocators.CLOSE_ORDER_DETAILS_BUTTON)

    def get_order_id(self):
        return self.get_text_from_element(OrderLocators.ORDER_ID)

    def is_order_visible_in_feed(self, order_id):
        locator = self.find_and_format_locator(
            (By.XPATH, "//p[contains(text(),'{}')]"),
            order_id
        )
        return self.is_element_visible(locator)

    def is_order_in_progress(self, order_id):
        locator = self.find_and_format_locator(
            (By.XPATH, "//p[contains(text(),'{}')]/following::p[contains(text(),'Готовится')]"),
            order_id
        )
        return self.is_element_visible(locator)

    def get_orders_in_progress(self):
        return [el.text for el in self.driver.find_elements(*OrderLocators.ORDERS_IN_PROGRESS)]

    def is_order_in_progress(self, order_id):
        return order_id in self.get_orders_in_progress()


    def click_feed(self):

        self.click_to_element(OrderLocators.ORDER_FEED_BUTTON)

    def is_order_in_progress(self, order_number):
        locator = (OrderLocators.ORDER_IN_PROGRESS[0],
                   OrderLocators.ORDER_IN_PROGRESS[1].format(order_number))
        try:
            return self.is_element_visible(locator)
        except:
            return False

    def wait_for_order_in_progress(self, order_number, timeout=10):
        locator = (OrderLocators.ORDER_IN_PROGRESS[0],
                   OrderLocators.ORDER_IN_PROGRESS[1].format(order_number))
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def get_order_id_from_details(self):
        self.find_and_wait_until_text_changes(OrderLocators.ORDER_ID, "9999")
        return self.get_text_from_element(OrderLocators.ORDER_ID)