FINAL PROJECT - ORDER APP

Тема:
Order management / управление заказами.

Структура:
final_order_oop/
    main.py
    order_module.py
    test_order_module.py
    settings.ini
    exported_orders.csv
    exported_orders.json
    exported_orders.xml
    order_app.log
    screens/
    htmlcov/

Что реализовано:
1. OOP:
   - Order
   - OrderList
   - App
   - собственные классы ошибок

2. CRUD:
   - create
   - read
   - update
   - delete

3. Исключения:
   - BadIdError
   - BadCustomerError
   - BadProductError
   - BadQuantityError

4. Методы:
   - обычные методы
   - @classmethod
   - @staticmethod

5. Экспорт:
   - CSV
   - JSON
   - XML

6. Дополнительно:
   - configparser
   - logging
   - pytest tests
   - html coverage report
   - документация в docstring через тройные кавычки

Как запустить приложение:
python main.py

Как запустить тесты:
pytest -v

Как создать HTML coverage:
pytest --cov=order_module --cov-report=html

После этого отчет находится:
htmlcov/index.html
