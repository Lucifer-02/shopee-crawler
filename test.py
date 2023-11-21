from playwright.sync_api import Playwright, sync_playwright
from bs4 import BeautifulSoup
import json


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    with open("cookies.json", "r") as f:
        cookies = json.load(f)

    context.add_cookies(cookies)
    # https://www.zenrows.com/blog/stealth-web-scraping-in-python-avoid-blocking-like-a-ninja#headless-browsers
    page = context.new_page()
    page.goto(
        "https://shopee.vn/CARDIGAN-SENTINIALS-STRIPES-%C3%A1o-cardigan-i.314050421.19331826287?sp_atk=acd85a64-262a-490b-9076-eb7227b04c9c&xptdk=acd85a64-262a-490b-9076-eb7227b04c9c"
    )

    # page.evaluate("document.body.style.zoom=0.1")
    # page.wait_for_load_state("networkidle")

    # soup = BeautifulSoup(page.content(), "lxml")

    input()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
