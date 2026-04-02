import allure
import pytest

from pages.form_fields_page import FormFieldsPage


@allure.epic("Practice Automation")
@allure.feature("Form Fields")
class TestFormFields:

    @allure.title("Fill and submit form with all fields")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_fill_and_submit_form(self, driver):
        """
        Precondition: Open browser and navigate to form page.
        Steps:
          1. Fill in the Name field
          2. Fill in the Password field
          3. Select Milk and Coffee from drinks
          4. Select Yellow from colors
          5. Select 'Yes' for automation preference
          6. Fill Email with name@example.com
          7. Enter tool count in Message and the longest tool name
          8. Click Submit
        Expected: Alert with 'Message received!'
        """
        page = FormFieldsPage(driver)

        page.open()
        page.close_popup_if_present()

        (
            page
            .fill_name("Test User")
            .fill_password("SecurePass123")
            .select_drink_milk()
            .select_drink_coffee()
            .select_color_yellow()
            .select_automation("yes")
        )

        page.fill_email("testuser@example.com")

        tool_count, longest_tool = page.get_tool_count_and_longest()
        page.fill_message(f"{tool_count}, {longest_tool}")

        page.screenshot("form_before_submit")
        page.submit()

        with allure.step("Verify alert with 'Message received!' appears"):
            alert_text = page.get_alert_text()
            assert alert_text == "Message received!", f"Expected 'Message received!', got '{alert_text}'"
            page.accept_alert()


@allure.epic("Practice Automation")
@allure.feature("Form Validation")
class TestFormValidation:

    @allure.title("Positive: submit form with all required fields filled")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_positive_valid_submission(self, driver):
        """
        Positive test: fill all required fields with valid data and submit.
        Expected: Alert with 'Message received!'
        """
        page = FormFieldsPage(driver)
        page.open()
        page.close_popup_if_present()

        (
            page
            .fill_name("Valid User")
            .fill_password("Pass123")
            .select_drink_milk()
            .select_color_yellow()
            .select_automation("yes")
            .fill_email("valid@example.com")
            .fill_message("Test message")
        )

        page.submit()

        with allure.step("Verify alert with 'Message received!' appears"):
            alert_text = page.get_alert_text()
            assert alert_text == "Message received!", f"Expected 'Message received!', got '{alert_text}'"
            page.accept_alert()

        page.screenshot("positive_test_result")

    @allure.title("Negative: submit form with empty required Name field")
    @allure.severity(allure.severity_level.NORMAL)
    def test_negative_empty_name(self, driver):
        """
        Negative test: leave the required Name field empty and submit.
        Expected: Form is NOT submitted, browser shows validation error.
        """
        page = FormFieldsPage(driver)
        page.open()
        page.close_popup_if_present()

        (
            page
            .fill_password("Pass123")
            .select_drink_coffee()
            .select_color_yellow()
            .select_automation("no")
            .fill_email("user@example.com")
            .fill_message("Test")
        )

        page.submit()

        with allure.step("Verify no alert appears (form not submitted)"):
            assert not page.is_alert_present(), "Alert should NOT appear when Name is empty"

        with allure.step("Verify browser validation message on Name field"):
            msg = page.get_validation_message(FormFieldsPage.NAME_INPUT)
            assert len(msg) > 0, "Validation message should be shown for empty Name"

        page.screenshot("negative_test_result")
