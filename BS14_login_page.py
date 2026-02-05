from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.browserstack.com"


def test_login_page_redirect(driver):
    driver.get(BASE_URL)

    login = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Sign in"))
    )
    login.click()

    WebDriverWait(driver, 10).until(EC.url_contains("sign_in"))
    assert "sign_in" in driver.current_url


def test_invalid_login_error_message(driver):
    driver.get("https://www.browserstack.com/users/sign_in")

    driver.find_element(By.ID, "user_email_login").send_keys("fake@email.com")
    driver.find_element(By.ID, "user_password").send_keys("wrongpassword")
    driver.find_element(By.NAME, "commit").click()

    assert "Invalid" in driver.page_source
