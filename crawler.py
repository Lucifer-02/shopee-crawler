from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://shopee.vn/Th%E1%BB%9Di-Trang-Nam-cat.11035567")
    page.evaluate("document.body.style.zoom=0.1")
    page.wait_for_load_state("networkidle")

    items = page.get_by_role("main").get_by_role("listitem").get_by_role("link").all()

    for item in items:
        item.get_attribute("href")

    assert len(items) == 60

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
