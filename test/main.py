import undetected_chromedriver as uc

import get_item_sources
import parse_source as ps

def main():
    with open("urls.txt", "r") as f:
        urls = f.readlines()
    print("number of urls: ", len(urls))

    driver = uc.Chrome(headless=True)
    sources = get_item_sources.get_item_sources(driver, urls=urls)
    print("sources len:", len(sources))
    for source in sources:
        item, _ = ps.parse_item_source(source=source)
        print(item)


if __name__ == "__main__":
    main()
