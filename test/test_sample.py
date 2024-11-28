
def test_sample():
    assert 1 == 1

def test_playwright(browser):
    browser.goto('https://www.google.com')
    assert browser.title() == 'Google'

def test_playwright_fail(browser):
    browser.goto('https://www.google.com')
    assert False