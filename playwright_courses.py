from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    registration_email_input.fill('user.name@gmail.com')

    registration_username_input = page.get_by_test_id("registration-form-username-input").locator('input')
    registration_username_input.fill('username')

    registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    registration_password_input.fill('password')

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    page.wait_for_url('**/#/dashboard', wait_until='networkidle')

    context.storage_state(path="browser-state.json")

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    courses_page_title = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_page_title).to_be_visible()
    expect(courses_page_title).to_have_text('Courses')

    courses_icon_empty = page.get_by_test_id('courses-list-empty-view-icon')
    expect(courses_icon_empty).to_be_visible()

    courses_title_empty = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(courses_title_empty).to_be_visible()
    expect(courses_title_empty).to_have_text('There is no results')

    courses_description_empty = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(courses_description_empty).to_be_visible()
    expect(courses_title_empty).to_have_text('Results from the load test pipeline will be displayed here')
