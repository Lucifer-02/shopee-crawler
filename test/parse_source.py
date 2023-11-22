from bs4 import BeautifulSoup


def parse_item_source(source: str) -> tuple[dict, list[str]]:
    assert source is not None

    soup = BeautifulSoup(source, "lxml")

    name = soup.find("div", class_="_44qnta").get_text()
    rate = soup.find("div", class_="_1k47d8 _046PXf").get_text()
    price = soup.find("div", class_="pqTWkA").get_text()
    sold = soup.find("div", class_="e9sAa2").get_text()
    link = soup.find('link', rel='canonical')

    suggest_links = []
    suggest_items = soup.find_all("div", class_="D-5l+y")
    for item in suggest_items:
        link = item.find("a").get("href")
        assert link is not None
        suggest_links.append(link)

    assert name is not None
    assert rate is not None
    assert price is not None
    assert sold is not None

    return {
        "url": link,
        "name": name,
        "rate": rate,
        "price": price,
        "sold": sold,
    }, suggest_links


def parse_cat_source(source: str) -> list[str]:
    links = []
    soup = BeautifulSoup(source, "lxml")

    items = soup.find_all("li", class_="col-xs-2-4 shopee-search-item-result__item")

    for item in items:
        link = item.find("a").get("href")
        assert link is not None
        links.append(link)

    assert len(items) == 60

    return links


def main():
    with open("./item.html", "r") as f:
        source = f.read()
    print(parse_item_source(source=source))


if __name__ == "__main__":
    main()
