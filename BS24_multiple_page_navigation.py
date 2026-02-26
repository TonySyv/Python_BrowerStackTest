def test_multiple_page_navigation(driver):
    driver.get("https://www.browserstack.com/")
    driver.get("https://www.browserstack.com/pricing")
    driver.get("https://www.browserstack.com/customers")

    assert "customers" in driver.current_url
