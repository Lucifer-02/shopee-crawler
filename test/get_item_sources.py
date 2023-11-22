import json
import random
from time import sleep

import numpy as np
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

# Initializing a list with two Useragents
useragentarray = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15",
]


def get_item_sources(driver: uc.Chrome, urls: list[str]) -> list[str]:
    sources = []
    for url in urls:
        # print(url)
        # with open("cookies.json", "r") as f:
        #     cookies = json.load(f)
        #     for cookie in cookies:
        driver.execute_cdp_cmd(
            "Network.setUserAgentOverride",
            {"userAgent": useragentarray[random.choice(range(len(useragentarray)))]},
        )
        driver.get(url)

        # Set zoom level
        driver.execute_script("document.body.style.zoom='4%'")

        sleep(random.choice([1, 2, 3]))

        try:
            # wait for Xem thêm appear
            WebDriverWait(driver, 3).until(
                EC.presence_of_element_located(
                    (
                        By.CSS_SELECTOR,
                        ".btn.btn-light.btn--m.btn--inline.btn-light--link.ofRWSV",
                    )
                )
            )
        except TimeoutException as e:
            print("Not found element in time: ", e)
            continue
        sources.append(driver.page_source)

    # input("Press any key to end...")
    driver.quit()

    return sources


def main():
    with open("urls.txt", "r") as f:
        urls = f.readlines()

    # start web driver
    driver = uc.Chrome(headless=False, use_subprocess=False)
    sources = get_item_sources(driver=driver, urls=urls)
    # with open("item.html", "w") as f:
    #     f.write(driver.page_source)


if __name__ == "__main__":
    main()
