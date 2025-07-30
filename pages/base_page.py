from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    @allure.step('нажать на элемент')
    def click_to_element(self, locator):
        element = WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable(locator)
        )
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('найти элемент')
    def find_element_with_wait(self, locator, timeout=35):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    @allure.step('найти текст на элементе')
    def add_text_to_element(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.clear()
        element.send_keys(text)

    def click_when_clickable(self, locator):
        WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable(locator)
        )
        self.driver.find_element(*locator).click()

    @allure.step('получить текст с элемента')
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step('проверить видимость элемента')
    def is_element_visible(self, locator, timeout=5):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            ).is_displayed()
        except TimeoutException:
            return False

    @allure.step('подождать пока элемент станет видимым')
    def wait_for_element_visible(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step('перейти по url')
    def navigate_to(self, url):
        self.driver.get(url)

    def wait_until_condition(self, condition, timeout=30):
        WebDriverWait(self.driver, timeout).until(condition)

    def find_and_wait_until_text_changes(self, locator, initial_text, timeout=30):
        self.wait_until_condition(
            lambda _: self.get_text_from_element(locator) != initial_text, timeout
        )
        return self.find_element_with_wait(locator)

    @allure.step('получаем атрибут элемента')
    def get_element_attribute(self, locator, attribute):
        return self.find_element_with_wait(locator).get_attribute(attribute)

    @allure.step('метод драг энд дропс, перетаскивание элемента')
    def drag_and_drop(self, source_locator, target_locator):
        source = self.find_element_with_wait(source_locator)
        target = self.find_element_with_wait(target_locator)

        if self.driver.name == 'firefox':
            script = """
                function simulateDragAndDrop(source, target) {
                    const dataTransfer = new DataTransfer();

                    function trigger(eventType, element) {
                        const event = new DragEvent(eventType, {
                            bubbles: true,
                            cancelable: true,
                            dataTransfer: dataTransfer,
                        });
                        element.dispatchEvent(event);
                    }

                    trigger('dragstart', source);
                    trigger('dragenter', target);
                    trigger('dragover', target);
                    trigger('drop', target);
                    trigger('dragend', source);
                }            
                simulateDragAndDrop(arguments[0], arguments[1]);
            """
            self.driver.execute_script(script, source, target)
        else:
            ActionChains(self.driver).drag_and_drop(source, target).perform()

    @allure.step('проверяем отображение элемента')
    def element_displayed(self, locator):
        try:
            element = self.find_element_with_wait(locator)
            return element.is_displayed()
        except TimeoutException:
            return False

    @allure.step('проверяем наличие элемента')
    def is_element_present(self, locator):
        return len(self.driver.find_elements(*locator)) > 0

    @allure.step('получаем текст элемента')
    def get_element_text(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step('найти элемент с ожиданием')
    def find_element_with_wait(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    @allure.step('нажать на элемент,когда загрузится')
    def click_element_when_ready(self, locator):
        WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()


    def is_current_url_contains(self, text):
        return text in self.driver.current_url

    def find_and_wait_until_text_changes(self, locator, initial_text, timeout=30):
        self.wait_until_condition(
            lambda _: self.get_text_from_element(locator) != initial_text, timeout
        )
        return self.find_element_with_wait(locator)

    @allure.step('Поиск списка элементов')
    def find_list(self, locators):
        return self.driver.find_elements(*locators)

    def find_and_format_locator(self, locator, dynamic_value):
        formatted_locator = self.format_locator(locator, dynamic_value)
        return self.find_element_with_wait(formatted_locator)

    @allure.step('Дождаться,когда эелемент станет видимым')
    def wait_visibility(self, locators):
        return self.wait.until(expected_conditions.visibility_of_element_located(locators))

    @allure.step('подождать пока элемент станет видимым')
    def wait_for_page_loaded(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )