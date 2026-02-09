def test_signup_page_load(driver):
    driver.get("https://www.browserstack.com/users/sign_up")
    assert "sign_up" in driver.current_url
