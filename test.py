from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://shopee.vn/Th%E1%BB%9Di-Trang-Nam-cat.11035567")
    # p = page.locator('xpath=//*[@id="main"]/div/div[2]/div/div/div[4]/div[2]/section/ul')
    # p = page.locator('xpath=/html/body/div[1]/div/div[2]/div/div/div[4]/div[2]/section/ul/li[1]')
    # item = page.locator('xpath=/html/body/div[1]/div/div[2]/div/div/div[4]/div[2]/section/ul/li[1]')
    # p = page.query_selector("#main > div > div:nth-child(3) > div > div > div.container.cZOmU2 > div.uXYBTq > section > ul")
    # print(item.text_content())
    # list_item = page.locator('xpath=/html/body/div[1]/div/div[2]/div/div/div[4]/div[2]/section/ul/li')
    # print(list_item.get_by_role('listitem').all())
    print(page.text_content(""))
    # print(list_item.text_content())
    # print(p.get_attribute('href'))
    # print(page.inner_html("body"))
    # page.get_by_text("Thông báoHỗ TrợTiếng ViệtĐăng KýĐăng Nhập").click()
    # page.get_by_role("link", name="Đăng Nhập").click()
    # page.get_by_placeholder("Email/Số điện thoại/Tên đăng nhập").click()
    # page.get_by_placeholder("Email/Số điện thoại/Tên đăng nhập").fill("18020574@vnu.edu.vn")
    # page.get_by_placeholder("Email/Số điện thoại/Tên đăng nhập").press("Tab")
    # page.get_by_placeholder("Mật khẩu").fill("Viethoang153.")
    # page.get_by_placeholder("Mật khẩu").press("Enter")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

