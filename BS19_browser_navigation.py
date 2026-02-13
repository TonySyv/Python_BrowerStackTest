BASE_URL = "https://www.browserstack.com"


def test_browser_back_functionality(driver):
    driver.get(BASE_URL)
    driver.get(f"{BASE_URL}/pricing")
    driver.back()

    assert BASE_URL in driver.current_url
