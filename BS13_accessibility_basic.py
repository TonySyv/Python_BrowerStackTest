from selenium.webdriver.common.by import By

def test_images_have_alt_text(driver):
    driver.get("https://www.browserstack.com/")
    images = driver.find_elements(By.TAG_NAME, "img")

    images_with_alt = [
        img for img in images if img.get_attribute("alt")
    ]

    assert len(images_with_alt) > 0
