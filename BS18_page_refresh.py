BASE_URL = "https://www.browserstack.com"


def test_page_refresh_stability(driver):
    driver.get(BASE_URL)
    driver.refresh()
    assert "BrowserStack" in driver.title
