from selenium.webdriver.common.by import By

def test_twitter_link(driver):
    driver.get("https://www.browserstack.com/")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    twitter = driver.find_element(By.XPATH, "//a[contains(@href,'twitter.com')]")
    href = twitter.get_attribute("href")

    assert "twitter.com" in href
