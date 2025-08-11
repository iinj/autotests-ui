from playwright.sync_api import expect, Page
import pytest


@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(chromium_page_with_state: Page):
    chromium_page_with_state.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    header = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(header).to_be_visible()
    expect(header).to_have_text('Courses')

    icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(icon).to_be_visible()

    text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(text).to_be_visible()
    expect(text).to_have_text('There is no results')

    description = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(description).to_be_visible()
    expect(description).to_have_text('Results from the load test pipeline will be displayed here')
