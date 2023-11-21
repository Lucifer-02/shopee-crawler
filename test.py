import json
from time import sleep

from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.firefox.launch(
        headless=False,
        proxy={"server": "http://127.0.0.1:8080"},
    )
    context = browser.new_context()
    with open("cookies.json", "r") as f:
        cookies = json.load(f)

    context.add_cookies(cookies)
    page = context.new_page()
    # page.set_extra_http_headers(headers)

    urls = [
        "https://shopee.vn",
        "https://shopee.vn/Th%E1%BB%9Di-Trang-Nam-cat.11035567",
        "https://shopee.vn/%C3%81o-Thun-Levents-Loveyou300k-Special-Cream-i.317477677.8603428111?sp_atk=0bb59b95-94fe-4a1e-9f6e-286cec7eb387&xptdk=0bb59b95-94fe-4a1e-9f6e-286cec7eb387",
        "https://shopee.vn/%C3%81o-Sweater-N%E1%BB%89-In-H%C3%ACnh-T%E1%BB%94NG-H%E1%BB%A2P-Si%C3%AAu-Xinh-Nhi%E1%BB%81u-M%C3%A0u-i.276087485.15012594597?sp_atk=b59bddad-3b12-4e94-95ae-6bff4e179a90&xptdk=b59bddad-3b12-4e94-95ae-6bff4e179a90",
        "https://shopee.vn/%C3%81o-Kho%C3%A1c-N%E1%BB%89-Sweater-In-Ch%E1%BB%AF-SEA-Si%C3%AAu-Xinh-Nhi%E1%BB%81u-M%C3%A0u-Unisex-i.276087485.10775665215?sp_atk=a7649e05-f9a5-4cd2-810e-951d389c7561&xptdk=a7649e05-f9a5-4cd2-810e-951d389c7561",
    ]

    page.goto(url=urls[1])

    # page.evaluate("document.body.style.zoom=0.1")
    page.wait_for_timeout(30000)
    # page.wait_for_load_state("networkidle")

    input()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
