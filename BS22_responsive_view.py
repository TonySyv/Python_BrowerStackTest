BASE_URL = "https://www.browserstack.com"


def test_mobile_screen_view(driver):
    driver.set_window_size(375, 812)
    driver.get(BASE_URL)

    assert "BrowserStack" in driver.title
