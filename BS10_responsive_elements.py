def test_mobile_view_navigation(driver):
    driver.set_window_size(375, 812)  # iPhone X size
    driver.get("https://www.browserstack.com/")
    assert "BrowserStack" in driver.title
