# SDET Autotests — Practice Automation Form

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run Tests

```bash
pytest tests/ -v
```

## Allure Report

```bash
allure serve allure-results
```

## Test Cases

### Test 1: Открыть и отправить форму (`test_fill_and_submit_form`)

**Precondition:** Open browser, navigate to https://practice-automation.com/form-fields/

| Step | Action | Expected |
|------|--------|----------|
| 1 | Fill Name field with "Test User" | Field contains value |
| 2 | Fill Password field with "SecurePass123" | Field contains value |
| 3 | Select Milk and Coffee from "What is your favorite drink?" | Both checkboxes selected |
| 4 | Select Yellow from "What is your favorite color?" | Yellow radio selected |
| 5 | Select "Yes" from "Do you like automation?" dropdown | "Yes" selected |
| 6 | Fill Email field with "testuser@example.com" | Field contains value |
| 7 | Count tools in "Automation tools" list, enter count and longest tool name in Message | Message contains "5, Katalon Studio" |
| 8 | Click Submit | Alert with text "Message received!" appears |

### Test 2 — Позитивная валидация (`test_positive_valid_submission`)

**Precondition:** Open browser, navigate to form page.

| Step | Action | Expected |
|------|--------|----------|
| 1 | Fill Name with "Valid User" | Field contains value |
| 2 | Fill Password with "Pass123" | Field contains value |
| 3 | Select Milk from drinks | Checkbox selected |
| 4 | Select Yellow from colors | Radio selected |
| 5 | Select "Yes" from automation dropdown | "Yes" selected |
| 6 | Fill Email with "valid@example.com" | Field contains value |
| 7 | Fill Message with "Test message" | Field contains value |
| 8 | Click Submit | Alert with text "Message received!" appears |

### Test 3 — Негативная валидация (`test_negative_empty_name`)

**Precondition:** Open browser, navigate to form page.

| Step | Action | Expected |
|------|--------|----------|
| 1 | Leave Name field empty | Field is empty |
| 2 | Fill Password with "Pass123" | Field contains value |
| 3 | Select Coffee from drinks | Checkbox selected |
| 4 | Select Yellow from colors | Radio selected |
| 5 | Select "No" from automation dropdown | "No" selected |
| 6 | Fill Email with "user@example.com" | Field contains value |
| 7 | Fill Message with "Test" | Field contains value |
| 8 | Click Submit | Form is NOT submitted; browser validation error on Name field |
