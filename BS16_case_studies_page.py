BASE_URL = "https://www.browserstack.com"


def test_customers_page_load(driver):
    driver.get(f"{BASE_URL}/customers")
    assert "customers" in driver.current_url
