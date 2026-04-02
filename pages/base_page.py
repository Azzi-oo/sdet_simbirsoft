import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class BasePage:

    def __init__(self, driver: WebDriver, url: str = ""):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, 10)

    def open(self) -> "BasePage":
        with allure.step(f"Open page: {self.url}"):
            self.driver.get(self.url)
        return self

    def find(self, locator: tuple) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_clickable(self, locator: tuple) -> WebElement:
        return self.wait.until(EC.element_to_be_clickable(locator))

    def scroll_to(self, locator: tuple) -> "BasePage":
        element = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        return self

    def click(self, locator: tuple) -> "BasePage":
        element = self.find_clickable(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        try:
            element.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", element)
        return self

    def type_text(self, locator: tuple, text: str) -> "BasePage":
        element = self.find(locator)
        element.clear()
        element.send_keys(text)
        return self

    def select_by_value(self, locator: tuple, value: str) -> "BasePage":
        element = self.find(locator)
        Select(element).select_by_value(value)
        return self

    def get_selected_option_text(self, locator: tuple) -> str:
        element = self.find(locator)
        return Select(element).first_selected_option.text

    def is_selected(self, locator: tuple) -> bool:
        return self.find(locator).is_selected()

    def get_attribute_value(self, locator: tuple, attr: str) -> str:
        return self.find(locator).get_attribute(attr)

    def get_alert_text(self) -> str:
        alert = self.wait.until(EC.alert_is_present())
        return alert.text

    def accept_alert(self) -> "BasePage":
        alert = self.wait.until(EC.alert_is_present())
        alert.accept()
        return self

    def is_alert_present(self, timeout: int = 3) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
            return True
        except Exception:
            return False

    def get_validation_message(self, locator: tuple) -> str:
        element = self.find(locator)
        return self.driver.execute_script("return arguments[0].validationMessage;", element)

    def screenshot(self, name: str = "screenshot") -> "BasePage":
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG,
        )
        return self
