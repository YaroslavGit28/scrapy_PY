def build_scrapy_settings() -> dict:
    return {
        "ROBOTSTXT_OBEY": True,
        "CONCURRENT_REQUESTS": 8,
        "DOWNLOAD_DELAY": 0.25,
        "AUTOTHROTTLE_ENABLED": True,
        "FEEDS": {
            "products.json": {
                "format": "json",
                "encoding": "utf8",
                "indent": 2,
                "overwrite": True,
            }
        },
    }


def run() -> None:
    print("\n=== DEMO 5: Settings и экспорт ===")
    settings = build_scrapy_settings()
    print("ROBOTSTXT_OBEY:", settings["ROBOTSTXT_OBEY"])
    print("CONCURRENT_REQUESTS:", settings["CONCURRENT_REQUESTS"])
    print("DOWNLOAD_DELAY:", settings["DOWNLOAD_DELAY"])
    print("FEEDS target:", list(settings["FEEDS"].keys())[0])


if __name__ == "__main__":
    run()
