from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators()

    def click_constructor_button(self):
        self.click_to_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    def is_burger_constructor_visible(self):
        return self.find_element_with_wait(MainPageLocators.BURGER_CONSTRUCTOR_SECTION).is_displayed()

    def get_constructor_title(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.CONSTRUCTOR_TITLE)
        ).text

    def click_order_feed(self):
        self.click_to_element(MainPageLocators.ORDER_FEED_BUTTON)

    def click_ingredient(self):
        self.click_to_element(MainPageLocators.INGREDIENT_KRATORNAYA)

    def close_modal(self):
        self.click_to_element(MainPageLocators.MODAL_CLOSE_BUTTON)

    def close_ingredient_modal(self):
        self.click_to_element(MainPageLocators.CLOSE_INGREDIENT_DETAILS_BUTTON)

    def ingredient_details_visible(self):
        return self.element_displayed(MainPageLocators.CLOSE_INGREDIENT_DETAILS_BUTTON)

    def open_main_page(self):
        self.driver.get("https://stellarburgers.nomoreparties.site")

    def get_ingredient_counter(self):
        return int(self.get_text_from_element(MainPageLocators.INGREDIENT_COUNTER))

    def get_order_number(self):
        return self.driver.find_element(*MainPageLocators.ORDER_NUMBER).text

    def select_buns_section(self):
        self.click_to_element(MainPageLocators.BUNS_SECTION)

    def select_sauces_section(self):
        self.click_to_element(MainPageLocators.SAUCES_SECTION)

    def select_toppings_section(self):
        self.click_to_element(MainPageLocators.TOPPINGS_SECTION)

    def select_ingredient(self, ingredient_type):
        locator = self.get_ingredient_locator(ingredient_type)
        if not locator:
            raise ValueError(f"Неизвестный тип ингредиента: {ingredient_type}")
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def get_ingredient_locator(self, ingredient_name):
        return MainPageLocators.get_ingredient_locator(ingredient_name)


    def get_constructor_area(self):
        return self.driver.find_element(*MainPageLocators.CONSTRUCTOR_AREA)

    def drag_ingredient_to_constructor(self):
        self.drag_and_drop(
            source_locator=self.locators.INGREDIENT_ITEM,
            target_locator=self.locators.CONSTRUCTOR_AREA
        )
    def click_place_order(self):
        self.driver.find_element(*MainPageLocators.PLACE_ORDER_BUTTON).click()

    def wait_for_page_loaded(self):
        WebDriverWait(self.driver, self.timeout).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

    def get_constructor_title(self):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(MainPageLocators.CONSTRUCTOR_TITLE)
        ).text

    def click_order_feed(self):
        self.click_to_element(MainPageLocators.ORDER_FEED_BUTTON)

    def click_order_feed(self):
        self.click_to_element(MainPageLocators.ORDER_FEED_BUTTON)

    def get_bun_counter(self):
        try:
            counter = self.driver.find_element(*MainPageLocators.BUN_COUNTER)
            return int(counter.text) if counter.text else 0
        except:
            return 0

    def get_count_value(self):
        try:
            counter = self.driver.find_element(*self.COUNTER_LOCATOR)
            return int(counter.text)
        except:
            return 0  # Если счетчик не найден, считаем что 0

    def add_filling_to_order(self):
        add_button = self.driver.find_element(*self.ADD_BUTTON_LOCATOR)
        add_button.click()
        time.sleep(1)

    def add_bun_standard_drag(self):
        self.drag_and_drop(
            MainPageLocators.INGREDIENT_KRATORNAYA,
            MainPageLocators.CONSTRUCTOR_AREA
        )

    def add_bun_seletools_drag(self):
        self.drag_and_drop_seletools(
            MainPageLocators.INGREDIENT_KRATORNAYA,
            MainPageLocators.CONSTRUCTOR_AREA
        )

    def is_bun_in_constructor(self):
        try:
            return len(self.driver.find_elements(*MainPageLocators.ADDED_INGREDIENT)) > 0
        except:
            return False

    def close_ingredient_details(self):
        self.click_to_element(MainPageLocators.CLOSE_INGREDIENT_DETAILS_BUTTON)