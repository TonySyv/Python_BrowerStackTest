def test_small_screen_view(driver):
    driver.set_window_size(300, 600)
    driver.get("https://www.browserstack.com/")
    assert driver.title != ""
