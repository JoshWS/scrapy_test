import scrapy


class BananaSpider(scrapy.Spider):
    name = "banana"
    start_urls = [
        "https://www.bnn.in.th/en/p?q=RTX&in_stock=true&sort_by=relevance&page=1"
    ]

    def parse(self, response):
        for products in response.css("div.product-item-details"):
            yield {
                "name": products.css("div.product-name::text")
                .get()
                .replace("\n", "")
                .replace("\u0e01\u0e32\u0e23\u0e4c\u0e14\u0e08\u0e2d", "")
                .strip(),
                "price": products.css("div.product-price::text")
                .get()
                .replace("\n", "")
                .replace("\u0e3f", "")
                .strip(),
            }
