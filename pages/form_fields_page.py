import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class FormFieldsPage(BasePage):

    URL = "https://practice-automation.com/form-fields/"

    NAME_INPUT = (By.ID, "name-input")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")

    DRINK_MILK = (By.ID, "drink2")
    DRINK_COFFEE = (By.ID, "drink3")

    COLOR_YELLOW = (By.CSS_SELECTOR, "input#color3")

    AUTOMATION_SELECT = (By.ID, "automation")

    TOOL_LIST_ITEMS = (By.XPATH, "//label[contains(text(),'Automation tools')]/following-sibling::ul/li")

    EMAIL_INPUT = (By.CSS_SELECTOR, "#email")
    MESSAGE_TEXTAREA = (By.CSS_SELECTOR, "#message")
    SUBMIT_BUTTON = (By.XPATH, "//button[@id='submit-btn']")

    POPUP_CLOSE = (By.CSS_SELECTOR, "button.pum-close")

    def __init__(self, driver: WebDriver):
        super().__init__(driver, self.URL)


    @allure.step("Close cookie popup if present")
    def close_popup_if_present(self) -> "FormFieldsPage":
        try:
            buttons = self.driver.find_elements(*self.POPUP_CLOSE)
            for btn in buttons:
                if btn.is_displayed():
                    btn.click()
                    break
        except Exception:
            pass
        return self

    @allure.step("Fill Name field with: {name}")
    def fill_name(self, name: str) -> "FormFieldsPage":
        self.type_text(self.NAME_INPUT, name)
        return self

    @allure.step("Fill Password field")
    def fill_password(self, password: str) -> "FormFieldsPage":
        self.type_text(self.PASSWORD_INPUT, password)
        return self

    @allure.step("Select drink: Milk")
    def select_drink_milk(self) -> "FormFieldsPage":
        self.click(self.DRINK_MILK)
        return self

    @allure.step("Select drink: Coffee")
    def select_drink_coffee(self) -> "FormFieldsPage":
        self.click(self.DRINK_COFFEE)
        return self

    @allure.step("Select color: Yellow")
    def select_color_yellow(self) -> "FormFieldsPage":
        self.click(self.COLOR_YELLOW)
        return self

    @allure.step("Select automation option: {value}")
    def select_automation(self, value: str) -> "FormFieldsPage":
        self.select_by_value(self.AUTOMATION_SELECT, value)
        return self

    @allure.step("Get automation tool count and longest tool name")
    def get_tool_count_and_longest(self) -> tuple:
        items = self.driver.find_elements(*self.TOOL_LIST_ITEMS)
        tool_names = [item.text.strip() for item in items]
        longest = max(tool_names, key=len)
        return len(tool_names), longest

    @allure.step("Fill Email field with: {email}")
    def fill_email(self, email: str) -> "FormFieldsPage":
        self.type_text(self.EMAIL_INPUT, email)
        return self

    @allure.step("Fill Message field with: {message}")
    def fill_message(self, message: str) -> "FormFieldsPage":
        self.type_text(self.MESSAGE_TEXTAREA, message)
        return self

    @allure.step("Clear Name field")
    def clear_name(self) -> "FormFieldsPage":
        element = self.find(self.NAME_INPUT)
        element.clear()
        return self

    @allure.step("Click Submit button")
    def submit(self) -> "FormFieldsPage":
        self.click(self.SUBMIT_BUTTON)
        return self
