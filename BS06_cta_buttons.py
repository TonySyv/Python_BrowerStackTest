from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.browserstack.com"


def test_free_trial_cta_visible(driver):
    driver.get(BASE_URL)

    free_trial = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Free Trial')]"))
    )

    assert free_trial.is_displayed()
