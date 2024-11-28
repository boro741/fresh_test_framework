import os
import pytest
from playwright.sync_api import sync_playwright
import pytest_html
import allure

@pytest.fixture
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs["browser"]
        if page:
            project_root = os.path.abspath(os.path.dirname(__file__))
            screenshot_path = os.path.join(project_root, f"screenshots/{item.name}.png")
            page.screenshot(path=screenshot_path)

        if not hasattr(rep,'extra'):
            rep.extra = []
        #Pytest-html integration
        # rep.extra.append(pytest_html.extras.image(screenshot_path))
        # Allure Integration
        with open(screenshot_path, "rb") as image_file:
            allure.attach(image_file.read(), name=item.name, attachment_type=allure.attachment_type.PNG)