import httpx
from bs4 import BeautifulSoup, Tag, NavigableString


def get_xml() -> str:
    url = "https://xskt.com.vn/rss-feed/mien-nam-xsmn.rss"
    xml = httpx.get(url=url)
    return xml.text


def parse_xml(xml: str) -> str:
    lottery_result: str = ""
    try:
        soup: BeautifulSoup = BeautifulSoup(
            xml,
            features="xml",
        )
        # print(soup.find("item"))
        first_item = soup.find("item")

        if first_item:
            title_tag = first_item.title
            title: str = title_tag.text if title_tag else ""
            description_tag = first_item.find("description")
            description = (
                description_tag.text.replace("8: ", "\n8: ") if description_tag else ""  # type: ignore
            )

            lottery_result: str = f"{title}\n{description}"
    except Exception:
        pass

    return lottery_result


def get_newest_lottery_results() -> str:
    xml = get_xml()
    return parse_xml(xml)
