from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.browserstack.com"


def test_footer_links_present(driver):
    driver.get(BASE_URL)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    footer_links = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "footer a"))
    )

    assert len(footer_links) > 5
