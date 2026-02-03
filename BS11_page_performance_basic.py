import time


def test_homepage_load_time(driver):
    start = time.time()
    driver.get("https://www.browserstack.com/")
    load_time = time.time() - start

    assert load_time < 8  # seconds
