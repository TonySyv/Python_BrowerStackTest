from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.browserstack.com"


def test_products_menu_hover(driver):
    driver.get(BASE_URL)

    products = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.LINK_TEXT, "Products"))
    )

    ActionChains(driver).move_to_element(products).perform()

    live = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.LINK_TEXT, "Live"))
    )

    assert live.is_displayed()
