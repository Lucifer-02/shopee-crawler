import json
from time import sleep
import random

from playwright.sync_api import Playwright, sync_playwright
from bs4 import BeautifulSoup

urls = [
    "https://shopee.vn",
    "https://shopee.vn/Th%E1%BB%9Di-Trang-Nam-cat.11035567",
    "https://shopee.vn/Tws-Tai-Nghe-Ch%E1%BB%A5p-Tai-bluetooth-5.2-%C3%82m-Thanh-hifi-Ki%E1%BB%83u-D%C3%A1ng-Th%E1%BB%83-Thao-i.451212855.23252605785?sp_atk=cf6348ce-b860-4f3e-b4b5-4897a3eb7b7f&xptdk=cf6348ce-b860-4f3e-b4b5-4897a3eb7b7f",
    "https://shopee.vn/%C3%81o-Thun-Levents-Loveyou300k-Special-Cream-i.317477677.8603428111?sp_atk=0bb59b95-94fe-4a1e-9f6e-286cec7eb387&xptdk=0bb59b95-94fe-4a1e-9f6e-286cec7eb387",
    "https://shopee.vn/%C3%81o-Sweater-N%E1%BB%89-In-H%C3%ACnh-T%E1%BB%94NG-H%E1%BB%A2P-Si%C3%AAu-Xinh-Nhi%E1%BB%81u-M%C3%A0u-i.276087485.15012594597?sp_atk=b59bddad-3b12-4e94-95ae-6bff4e179a90&xptdk=b59bddad-3b12-4e94-95ae-6bff4e179a90",
    "https://shopee.vn/%C3%81o-Kho%C3%A1c-N%E1%BB%89-Sweater-In-Ch%E1%BB%AF-SEA-Si%C3%AAu-Xinh-Nhi%E1%BB%81u-M%C3%A0u-Unisex-i.276087485.10775665215?sp_atk=a7649e05-f9a5-4cd2-810e-951d389c7561&xptdk=a7649e05-f9a5-4cd2-810e-951d389c7561",
]


def get_links() -> list[str]:
    links = []
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
        )
        page = context.new_page()

        with open("./shopee.vn_cookies.json", "r") as f:
            cookies = json.load(f)
            context.add_cookies(cookies)

        page.goto(urls[2])
        page.evaluate("document.body.style.zoom=0.1")
        page.wait_for_load_state("networkidle")

        soup = BeautifulSoup(page.content(), "lxml")

        items = soup.find_all("li", class_="col-xs-2-4 shopee-search-item-result__item")

        for item in items:
            link = item.find("a").get("href")
            links.append(link)

        # assert len(items) == 60

        input("Enter any key to quit...")

        # ---------------------
        context.close()
        browser.close()
    return links


def main():
    links = get_links()
    with open("urls.txt", "w") as f:
        for link in links:
            f.write(f"{urls[0]}/{link}\n")


if __name__ == "__main__":
    main()
