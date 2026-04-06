import sys

from demo_01_basics import run as run_basics
from demo_02_selectors import run as run_selectors
from demo_03_spider_flow import run as run_spider_flow
from demo_04_items_pipelines import run as run_items_pipeline
from demo_05_settings_export import run as run_settings


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    print("scrapy-study-project: запуск всех учебных примеров")
    run_basics()
    run_selectors()
    run_spider_flow()
    run_items_pipeline()
    run_settings()


if __name__ == "__main__":
    main()
