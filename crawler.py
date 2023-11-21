from playwright.sync_api import Playwright, sync_playwright
from bs4 import BeautifulSoup


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://shopee.vn/Th%E1%BB%9Di-Trang-Nam-cat.11035567")
    page.evaluate("document.body.style.zoom=0.1")
    page.wait_for_load_state("networkidle")

    soup = BeautifulSoup(page.content(), "lxml")

    items = soup.find_all("li", class_="col-xs-2-4 shopee-search-item-result__item")

    for item in items:
        print(item.find("a").get("href"))

    assert len(items) == 60

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
