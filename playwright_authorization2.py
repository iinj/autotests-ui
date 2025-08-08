from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    chromium = playwright.chromium.launch(headless=False)
    page = chromium.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    email_input_auth = page.get_by_test_id('login-form-email-input').locator('input')
    expect(email_input_auth).to_be_visible()

    password_input_auth = page.get_by_test_id('login-form-password-input').locator('input')
    expect(password_input_auth).to_be_visible()

    login_button_auth = page.get_by_test_id('login-page-login-button')
    expect(login_button_auth).to_be_visible()

    registration_button_auth = page.get_by_test_id('login-page-registration-link')
    registration_button_auth.click()

    email_input_reg = page.get_by_test_id('registration-form-email-input').locator('input')
    expect(email_input_reg).to_be_visible()

    username_input_reg = page.get_by_test_id('registration-form-username-input').locator('input')
    expect(username_input_reg).to_be_visible()

    password_input_reg = page.get_by_test_id('registration-form-password-input').locator('input')
    expect(password_input_reg).to_be_visible()

    page.wait_for_timeout(5000)


