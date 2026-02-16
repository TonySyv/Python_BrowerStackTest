from selenium.webdriver.common.by import By

BASE_URL = "https://www.browserstack.com"


def test_images_have_src(driver):
    driver.get(BASE_URL)

    images = driver.find_elements(By.TAG_NAME, "img")
    for img in images:
        assert img.get_attribute("src") is not None
