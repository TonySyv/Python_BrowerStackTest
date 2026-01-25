BASE_URL = "https://www.browserstack.com"


def test_homepage_loads(driver):
    driver.get(BASE_URL)
    assert driver.current_url.startswith(BASE_URL)


def test_homepage_title(driver):
    driver.get(BASE_URL)
    assert "BrowserStack" in driver.title
