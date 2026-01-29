from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.browserstack.com"


def test_developers_link(driver):
    driver.get(BASE_URL)

    developers = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Developers"))
    )
    developers.click()

    WebDriverWait(driver, 10).until(EC.url_contains("developers"))
    assert "developers" in driver.current_url


def test_resources_link(driver):
    driver.get(BASE_URL)

    resources = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Resources"))
    )
    resources.click()

    WebDriverWait(driver, 10).until(EC.title_contains("Resources"))
    assert "Resources" in driver.title
