# scrapy-study-project

Учебный проект по библиотеке `scrapy` для Python.

Цель: показать, как устроен scraping-пайплайн в `scrapy` — от запроса и парсинга до items, pipelines и экспорта.

## Содержимое

- `src/run_all.py` — запуск всех демо.
- `src/demo_01_basics.py` — базовые сущности Scrapy.
- `src/demo_02_selectors.py` — CSS/XPath селекторы.
- `src/demo_03_spider_flow.py` — логика `start_requests`, `parse`, `follow`.
- `src/demo_04_items_pipelines.py` — Items и Pipeline.
- `src/demo_05_settings_export.py` — настройки и экспорт данных.
- `wiki/` — полный учебный курс (3 модуля, 15 глав, схемы, примеры).

## Быстрый старт

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python src/run_all.py
```

Подробная документация: `wiki/Home.md`.
