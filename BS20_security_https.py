BASE_URL = "https://www.browserstack.com"


def test_site_uses_https(driver):
    driver.get(BASE_URL)
    assert driver.current_url.startswith("https://")
