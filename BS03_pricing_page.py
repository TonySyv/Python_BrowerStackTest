from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.browserstack.com"


def test_pricing_page_navigation(driver):
    driver.get(BASE_URL)
    pricing = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Pricing"))
    )
    pricing.click()

    WebDriverWait(driver, 10).until(EC.title_contains("Pricing"))
    assert "Pricing" in driver.title
