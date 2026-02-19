import time

BASE_URL = "https://www.browserstack.com"


def test_homepage_load_time_under_8_seconds(driver):
    start_time = time.time()
    driver.get(BASE_URL)
    load_time = time.time() - start_time

    assert load_time < 8
