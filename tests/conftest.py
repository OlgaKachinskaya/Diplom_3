import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.account_page import AccountPage
from data import BASE_URL, EMAIL, PASSWORD


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        options = ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(options=options)
    elif request.param == 'firefox':
        options = FirefoxOptions()
        options.add_argument('--headless')
        driver = webdriver.Firefox(options=options)

    driver.implicitly_wait(10)
    driver.get(BASE_URL)

    yield driver
    driver.quit()


@pytest.fixture
def authorized_user(driver, account_page):
    account_page.click_account_button()
    account_page.enter_email(EMAIL)
    account_page.enter_password(PASSWORD)
    account_page.click_login()
    yield


@pytest.fixture
def created_order(driver, main_page, order_page):
    main_page.select_buns_section()
    main_page.drag_and_drop(main_page.get_ingredient_locator("Булочка"), main_page.get_constructor_area())
    main_page.click_place_order()
    order_id = order_page.get_order_id()
    yield order_id

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def account_page(driver):
    return AccountPage(driver)
