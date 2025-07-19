from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import time


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_to_element(self, locator):
        element = WebDriverWait(self.driver, 25).until(
            EC.element_to_be_clickable(locator)
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    def find_element_with_wait(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def add_text_to_element(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.clear()
        element.send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def is_element_visible(self, locator, timeout=5):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            ).is_displayed()
        except TimeoutException:
            return False

    def wait_for_element_visible(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def navigate_to(self, url):
        self.driver.get(url)

    def find_and_wait_until_text_changes(self, locator, original_text, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.find_element(*locator).text != original_text
        )

    def get_element_attribute(self, locator, attribute):
        return self.find_element_with_wait(locator).get_attribute(attribute)

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

    def element_displayed(self, locator):
        try:
            element = self.find_element_with_wait(locator)
            return element.is_displayed()
        except TimeoutException:
            return False

    def is_element_present(self, locator):
        return len(self.driver.find_elements(*locator)) > 0

    def get_element_text(self, locator):
        return self.find_element_with_wait(locator).text

    def find_element_with_wait(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )