def test_meta_title_present(driver):
    driver.get("https://www.browserstack.com/")
    assert driver.title is not None
    assert len(driver.title) > 5


def test_meta_description_present(driver):
    driver.get("https://www.browserstack.com/")
    description = driver.find_element("xpath", "//meta[@name='description']")
    assert description.get_attribute("content") != ""
