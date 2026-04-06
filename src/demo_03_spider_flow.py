from scrapy import Request, Spider
from scrapy.http import TextResponse


class FlowSpider(Spider):
    name = "flow_spider"

    def start_requests(self):
        yield Request("https://example.com/catalog", callback=self.parse_catalog)

    def parse_catalog(self, response):
        links = response.css("a.product::attr(href)").getall()
        for link in links:
            yield response.follow(link, callback=self.parse_product)

    def parse_product(self, response):
        title = response.css("h1::text").get(default="N/A")
        yield {"url": response.url, "title": title}


def run() -> None:
    print("\n=== DEMO 3: Поток spider (start_requests -> parse -> follow) ===")
    spider = FlowSpider()
    start_req = next(spider.start_requests())
    print("Start request:", start_req.url)

    catalog_html = """
    <html><body>
      <a class="product" href="/products/1">P1</a>
      <a class="product" href="/products/2">P2</a>
    </body></html>
    """
    catalog_response = TextResponse(
        url=start_req.url, body=catalog_html, encoding="utf-8", request=start_req
    )
    next_requests = list(spider.parse_catalog(catalog_response))
    print("Follow requests count:", len(next_requests))
    for req in next_requests:
        print(" ->", req.url)


if __name__ == "__main__":
    run()
