def test_http_redirects_to_https(driver):
    driver.get("http://www.browserstack.com")
    assert driver.current_url.startswith("https://")
