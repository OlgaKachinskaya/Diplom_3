from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.order_locators import OrderLocators
import time
import allure

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators()

    @allure.step('нажимаем на кнопку констуртор')
    def click_constructor_button(self):
        self.click_to_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('лента заказов счетчик видна')
    def is_order_feed_counter_visible(self):
        return self.is_element_visible(MainPageLocators.COMPLETED_ORDERS)

    @allure.step('проверяем видимость конструктора бургеров')
    def is_burger_constructor_visible(self):
        return self.is_element_visible(MainPageLocators.BURGER_CONSTRUCTOR_SECTION)

    def id_order(self):
        return self.get_text_from_element(MainPageLocators.ID_ORDER)

    @allure.step('получаем заголовок конструктора')
    def get_constructor_title(self):
        return self.get_text_from_element(MainPageLocators.CONSTRUCTOR_TITLE)

    @allure.step('нажимаем кнопку лента заказов')
    def click_order_feed(self):
        self.click_to_element(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step('выбрать ингредиент')
    def click_ingredient(self):
        self.click_to_element(MainPageLocators.INGREDIENT_KRATORNAYA)

    @allure.step('закрываем модальное окно')
    def close_modal(self):
        self.click_element_when_ready(OrderLocators.CLOSE_ORDER_DETAILS_BUTTON)

    @allure.step('закрываем модальное окно деталей ингредиентов')
    def close_ingredient_modal(self):
        self.click_to_element(MainPageLocators.CLOSE_INGREDIENT_DETAILS_BUTTON)

    @allure.step('проверяем видимость деталей ингредиентов')
    def ingredient_details_visible(self):
        return self.is_element_visible(MainPageLocators.CLOSE_INGREDIENT_DETAILS_BUTTON)

    @allure.step('открыть главную страницу')
    def open_main_page(self):
        self.navigate_to("https://stellarburgers.nomoreparties.site")

    @allure.step('получить счетчик ингредиента')
    def get_ingredient_counter(self):
        return int(self.get_text_from_element(MainPageLocators.INGREDIENT_COUNTER))

    @allure.step('получить номер заказа')
    def get_order_number(self):
        return self.get_text_from_element(MainPageLocators.ORDER_NUMBER)

    @allure.step('выбрать раздел булки')
    def select_buns_section(self):
        self.click_to_element(MainPageLocators.BUNS_SECTION)

    @allure.step('выбрать раздел соусы')
    def select_sauces_section(self):
        self.click_to_element(MainPageLocators.SAUCES_SECTION)

    @allure.step('выбрать раздел начинки')
    def select_toppings_section(self):
        self.click_to_element(MainPageLocators.TOPPINGS_SECTION)

    @allure.step('выбрать ингредиент')
    def select_ingredient(self, ingredient_type):
        locator = self.get_ingredient_locator(ingredient_type)
        self.click_to_element(locator)

    @allure.step('выбрать локатор ингредиента')
    def get_ingredient_locator(self, ingredient_name):
        return MainPageLocators.get_ingredient_locator(ingredient_name)

    @allure.step('получить область конструктора')
    def get_constructor_area(self):
        return self.find_element_with_wait(MainPageLocators.CONSTRUCTOR_AREA)

    @allure.step('перетащить ингредиент в конструктор')
    def drag_ingredient_to_constructor(self):
        self.drag_and_drop(
            source_locator=self.locators.INGREDIENT_ITEM,
            target_locator=self.locators.CONSTRUCTOR_AREA
        )

    @allure.step('нажать оформить заказ')
    def click_place_order(self):
        self.click_to_element(MainPageLocators.PLACE_ORDER_BUTTON)

    @allure.step('получить счетчик булок')
    def get_bun_counter(self):
        try:
            counter_text = self.get_text_from_element(MainPageLocators.BUN_COUNTER)
            return int(counter_text) if counter_text else 0
        except:
            return 0

    @allure.step('добавить булку перетаскиванием')
    def add_bun_standard_drag(self):
        self.drag_and_drop(
            MainPageLocators.INGREDIENT_KRATORNAYA,
            MainPageLocators.CONSTRUCTOR_AREA
        )

    @allure.step('проверить наличие булки в конструкторе')
    def is_bun_in_constructor(self):
        return self.is_element_present(MainPageLocators.ADDED_INGREDIENT)