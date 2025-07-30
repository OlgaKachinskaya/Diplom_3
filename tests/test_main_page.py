import pytest
import allure
import time
from pages.base_page import BasePage
from pages.account_page import AccountPage
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import BASE_URL, LOGIN_URL, EMAIL, PASSWORD
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

@allure.feature('Тесты конструктора')
class TestConstructorNavigation:
    @allure.title('Переход в конструктор из личного кабинета')
    def test_constructor_navigation(self, driver):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        with allure.step('Открываем страницу входа'):
            account_page.open_login_page()

        with allure.step('Кликаем кнопку "Конструктор" в хедере'):
            main_page.click_constructor_button()

        with allure.step('Проверяем, что секция "Собери бургер" отображается'):
            assert main_page.is_burger_constructor_visible(), "Секция 'Собери бургер' не отображается!"

@allure.feature('Тесты навигации')
class TestNavigation:
    @allure.title('Проверка перехода в "Ленту заказов"')
    def test_order_feed_navigation(self, driver):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        with allure.step('Открываем страницу входа'):
            account_page.open_login_page()

        with allure.step('Нажимаем на кнопку "Лента заказов"'):
            main_page.click_order_feed()

        with allure.step('Проверяем отображение ленты заказов'):
            assert main_page.is_order_feed_counter_visible(), "Не перешли в ленту заказов"

@allure.feature('Тесты модальных окон')
class TestModalWindows:
    @allure.title('Проверка отображения модального окна ингредиента')
    def test_ingredient_modal_display(self, driver):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        with allure.step('Открываем главную страницу'):
            account_page.open_login_page()

        with allure.step('Нажимаем на "Конструктор"'):
            main_page.click_constructor_button()

        with allure.step('Нажимаем на ингредиент'):
            main_page.click_ingredient()

        with allure.step('Проверяем, что окно с деталями ингредиента отображается'):
            assert main_page.ingredient_details_visible(), "Модальное окно не отобразилось"

    @allure.title('Проверка закрытия модального окна ингредиента')
    def test_ingredient_modal_close(self, driver):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        with allure.step('Открываем главную страницу'):
            account_page.open_login_page()

        with allure.step('Нажимаем на "Конструктор"'):
            main_page.click_constructor_button()

        with allure.step('Нажимаем на ингредиент'):
            main_page.click_ingredient()

        with allure.step('Закрываем окно с деталями ингредиента'):
            main_page.close_modal()

        with allure.step('Проверяем, что окно с деталями ингредиента закрыто'):
            assert not main_page.ingredient_details_visible()

@allure.feature('Тесты конструктора бургеров')
class TestBurgerConstructor:
    @allure.title('Тест перетаскивание булки')
    def test_bun_drag_and_drop(self, driver):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        with allure.step('Открываем страницу главную'):
            account_page.open_login_page()

        with allure.step('Нажимаем на "Конструктор"'):
            main_page.click_constructor_button()

        with allure.step('Получаем начальное значение счетчика ингредиентов'):
            initial_counter = main_page.get_ingredient_counter()

        with allure.step('Перетаскиваем булку в конструктор'):
            main_page.drag_and_drop(
                MainPageLocators.INGREDIENT_KRATORNAYA,
                MainPageLocators.CONSTRUCTOR_AREA
            )

        with allure.step('Проверяем, что счетчик увеличился'):
            updated_counter = main_page.get_ingredient_counter()

        assert updated_counter == initial_counter + 2, \
            f"Каунтер не увеличился! Ожидалось: {initial_counter + 2}, но получено: {updated_counter}"