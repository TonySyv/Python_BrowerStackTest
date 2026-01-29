from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

RESOURCES_URL = "https://www.browserstack.com/resources"


def test_resources_page_loads(driver):
    driver.get(RESOURCES_URL)
    assert "resources" in driver.current_url


def test_blog_link_present(driver):
    driver.get(RESOURCES_URL)

    blog = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Blog"))
    )
    assert blog.is_displayed()
