import allure
import time
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.account_page import AccountPage
from locators.main_page_locators import MainPageLocators
from locators.order_locators import OrderLocators
from data import EMAIL, PASSWORD, BASE_URL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import allure
import time
from data import EMAIL, PASSWORD


@allure.feature('Лента заказов')
class TestOrderFeedCounter:
    @allure.title('Тест увеличения общего счётчика заказов')
    def test_total_orders_counter_increases_after_new_order(self, driver):
        order_page = OrderPage(driver)
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        with allure.step('1. открываем страницу'):
            main_page.open_main_page()

        with allure.step('2. Вход в аккаунт'):
            account_page.click_account_button()
            account_page.enter_email(EMAIL)
            account_page.enter_password(PASSWORD)
            account_page.click_login()
            time.sleep(3)

        with allure.step('3. Открываем ленту заказов'):

            order_page.click_feed()
            time.sleep(3)

        with allure.step('4. Получаем начальное значение счетчика'):
            initial_counter = order_page.get_total_orders_count()

        with allure.step('5. Создаем новый заказ'):
            main_page.click_constructor_button()
            time.sleep(2)

            main_page.drag_and_drop(
                MainPageLocators.INGREDIENT_KRATORNAYA,
                MainPageLocators.CONSTRUCTOR_AREA
            )
            time.sleep(2)

            main_page.click_place_order()
            time.sleep(5)

        with allure.step('5. Закрываем модальное окно заказа'):
            order_page.close_order_details()
            time.sleep(2)

        with allure.step('2. Открываем ленту заказов'):

            order_page.click_feed()
            time.sleep(3)


        with allure.step('6. Проверяем увеличение счетчика'):
            order_page.navigate_to_feed()
            time.sleep(3)
            updated_counter = order_page.get_total_orders_count()

            assert updated_counter > initial_counter, \
                f"Счетчик не увеличился. Было: {initial_counter}, стало: {updated_counter}"

    @allure.title('Тест увеличения счетчика "Выполнено за сегодня"')
    def test_today_orders_counter_increases_after_new_order(self, driver):
        # Инициализация страниц
        order_page = OrderPage(driver)
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        with allure.step('1. открываем страницу'):
            main_page.open_main_page()

        with allure.step('2. Вход в аккаунт'):
            account_page.click_account_button()
            account_page.enter_email(EMAIL)
            account_page.enter_password(PASSWORD)
            account_page.click_login()
            time.sleep(3)

        with allure.step('3. Открываем ленту заказов'):
            order_page.click_feed()
            time.sleep(3)

        with allure.step('4. Получаем начальное значение счетчика за сегодня'):
            initial_today_counter = order_page.get_today_orders_count()

        with allure.step('5. Создаем новый заказ'):
            main_page.click_constructor_button()
            time.sleep(2)

            main_page.drag_and_drop(
                MainPageLocators.INGREDIENT_KRATORNAYA,
                MainPageLocators.CONSTRUCTOR_AREA
            )
            time.sleep(2)

            main_page.click_place_order()
            time.sleep(5)

        with allure.step('6. Закрываем модальное окно заказа'):
            order_page.close_order_details()
            time.sleep(2)

        with allure.step('7. Проверяем увеличение счетчика за сегодня'):
            order_page.click_feed()
            time.sleep(3)

            updated_today_counter = order_page.get_today_orders_count()

            assert updated_today_counter > initial_today_counter, \
                f"Счетчик 'Выполнено за сегодня' не увеличился. Было: {initial_today_counter}, стало: {updated_today_counter}"


@allure.title('Тест появления номера заказа в разделе "В работе"')
def test_order_appears_in_progress_section(driver):
    order_page = OrderPage(driver)
    main_page = MainPage(driver)
    account_page = AccountPage(driver)

    with allure.step('1. Открываем страницу'):
        main_page.open_main_page()

    with allure.step('2. Выполняем вход в аккаунт'):
        account_page.click_account_button()
        account_page.enter_email(EMAIL)
        account_page.enter_password(PASSWORD)
        account_page.click_login()
        time.sleep(3)

    with allure.step('3. Открываем ленту заказов'):
        order_page.click_feed()
        time.sleep(3)

    with allure.step('4. Создаем новый заказ'):
        main_page.click_constructor_button()
        time.sleep(2)

        main_page.drag_and_drop(
            MainPageLocators.INGREDIENT_KRATORNAYA,
            MainPageLocators.CONSTRUCTOR_AREA
        )
        time.sleep(2)

        main_page.click_place_order()
        time.sleep(10)

    with allure.step('Получаем идентификатор заказа'):
        order_number = order_page.get_order_id_from_details()

    with allure.step('Закрываем модальное окно и проверяем раздел "В работе"'):
        order_page.close_order_details()
        time.sleep(2)

    with allure.step('3. Открываем ленту заказов'):
        order_page.click_feed()
        time.sleep(3)

    def is_order_number_in_progress(self, order_id):
        formatted_id = f"{int(order_number):07d}"
        self.find_and_format_locator(OrderLocators.ORDERS_IN_PROGRESS, formatted_id)
        return True