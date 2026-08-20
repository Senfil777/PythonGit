import csv
import json
import xml.etree.ElementTree as ET

import pytest

from order_module import (
    BadCustomerError,
    BadIdError,
    BadProductError,
    BadQuantityError,
    OrderList,
)


@pytest.fixture
def order_list():
    """Создает пустой список заказов для каждого теста."""
    OrderList.reset_id()
    return OrderList()


@pytest.fixture
def filled_order_list(order_list):
    """Создает список с двумя заказами."""
    order_list.create("Filip", "Laptop", 1)
    order_list.create("Anna", "Phone", 2)
    return order_list


def test_create_order(order_list):
    """Проверяет создание заказа."""
    order_id = order_list.create("Filip", "Laptop", 1)

    assert order_id == 1
    assert order_list.read(1).customer == "Filip"


def test_create_bad_customer(order_list):
    """Проверяет ошибку короткого имени клиента."""
    with pytest.raises(BadCustomerError):
        order_list.create("Al", "Laptop", 1)


def test_create_bad_product(order_list):
    """Проверяет ошибку короткого названия товара."""
    with pytest.raises(BadProductError):
        order_list.create("Filip", "PC", 1)


def test_create_bad_quantity(order_list):
    """Проверяет ошибку количества товара."""
    with pytest.raises(BadQuantityError):
        order_list.create("Filip", "Laptop", 0)


def test_read_order(filled_order_list):
    """Проверяет чтение заказа."""
    order = filled_order_list.read(1)

    assert order.product == "Laptop"
    assert order.quantity == 1


def test_read_bad_id(filled_order_list):
    """Проверяет отрицательный ID."""
    with pytest.raises(BadIdError):
        filled_order_list.read(-1)


def test_read_missing_id(filled_order_list):
    """Проверяет отсутствующий заказ."""
    with pytest.raises(BadIdError):
        filled_order_list.read(100)


def test_read_all(filled_order_list):
    """Проверяет вывод всех заказов."""
    result = filled_order_list.read_all()

    assert "Laptop" in result
    assert "Phone" in result


def test_update_order(filled_order_list):
    """Проверяет изменение заказа."""
    filled_order_list.update(1, "Filip", "Monitor", 2)

    order = filled_order_list.read(1)
    assert order.product == "Monitor"
    assert order.quantity == 2


def test_update_status(filled_order_list):
    """Проверяет изменение статуса."""
    filled_order_list.update_status(1, "done")

    assert filled_order_list.read(1).status == "done"


def test_update_bad_status(filled_order_list):
    """Проверяет недопустимый статус."""
    with pytest.raises(ValueError):
        filled_order_list.update_status(1, "unknown")


def test_delete_order(filled_order_list):
    """Проверяет удаление заказа."""
    assert filled_order_list.delete(1) is True

    with pytest.raises(BadIdError):
        filled_order_list.read(1)


def test_export_csv(filled_order_list, tmp_path):
    """Проверяет экспорт CSV."""
    file_name = tmp_path / "orders.csv"
    filled_order_list.export_csv(file_name)

    with open(file_name, newline="", encoding="utf-8") as file:
        rows = list(csv.reader(file))

    assert rows[0][0] == "id"
    assert rows[1][2] == "Laptop"


def test_export_json(filled_order_list, tmp_path):
    """Проверяет экспорт JSON."""
    file_name = tmp_path / "orders.json"
    filled_order_list.export_json(file_name)

    with open(file_name, encoding="utf-8") as file:
        data = json.load(file)

    assert data[0]["customer"] == "Filip"


def test_export_xml(filled_order_list, tmp_path):
    """Проверяет экспорт XML."""
    file_name = tmp_path / "orders.xml"
    filled_order_list.export_xml(file_name)

    root = ET.parse(file_name).getroot()

    assert root.tag == "orders"
    assert root[0].find("product").text == "Laptop"
