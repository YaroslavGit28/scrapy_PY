from scrapy import Request, Spider
from scrapy.http import TextResponse


class DemoSpider(Spider):
    name = "demo_spider"
    allowed_domains = ["example.com"]


def run() -> None:
    print("\n=== DEMO 1: Базовые сущности Scrapy ===")
    spider = DemoSpider()
    request = Request(url="https://example.com/catalog", callback=spider.parse)

    html = "<html><body><h1>Catalog</h1></body></html>"
    response = TextResponse(url=request.url, body=html, encoding="utf-8", request=request)

    print("Spider name:", spider.name)
    print("Request url:", request.url)
    print("Request method:", request.method)
    print("Response url:", response.url)
    print("Response status:", response.status)


if __name__ == "__main__":
    run()
