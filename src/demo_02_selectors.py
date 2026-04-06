from scrapy import Selector


def run() -> None:
    print("\n=== DEMO 2: CSS и XPath селекторы ===")
    html = """
    <html>
      <body>
        <div class="product" data-id="101">
          <a class="name" href="/p/101">Laptop Pro</a>
          <span class="price">1299</span>
        </div>
        <div class="product" data-id="102">
          <a class="name" href="/p/102">Mouse Air</a>
          <span class="price">49</span>
        </div>
      </body>
    </html>
    """

    sel = Selector(text=html)
    names_css = sel.css("div.product a.name::text").getall()
    first_href_css = sel.css("div.product a.name::attr(href)").get()
    ids_xpath = sel.xpath("//div[@class='product']/@data-id").getall()

    print("Names via CSS:", names_css)
    print("First href via CSS:", first_href_css)
    print("IDs via XPath:", ids_xpath)


if __name__ == "__main__":
    run()
