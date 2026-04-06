from dataclasses import dataclass


@dataclass
class ProductItem:
    title: str
    price: float
    currency: str


class NormalizePricePipeline:
    def process_item(self, item: ProductItem):
        if item.price < 0:
            raise ValueError("Price must be non-negative")
        item.price = round(float(item.price), 2)
        return item


def run() -> None:
    print("\n=== DEMO 4: Items и Pipelines ===")
    raw_item = ProductItem(title="Laptop Pro", price=1299.4999, currency="USD")
    pipeline = NormalizePricePipeline()
    clean_item = pipeline.process_item(raw_item)

    print("Raw/Clean item result:")
    print(clean_item)


if __name__ == "__main__":
    run()
