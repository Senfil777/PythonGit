import csv
import json
import xml.etree.ElementTree as ET


class BadIdError(Exception):
    """Ошибка для неверного ID заказа."""

    def __init__(self, order_id, message):
        """Сохраняет ID и сообщение об ошибке."""
        self.order_id = order_id
        self.message = message

    def __str__(self):
        """Возвращает понятный текст ошибки."""
        return f"BadIdError: id: {self.order_id}, message: {self.message}"


class BadCustomerError(Exception):
    """Ошибка для неверного имени клиента."""

    def __init__(self, customer, message):
        """Сохраняет имя клиента и сообщение об ошибке."""
        self.customer = customer
        self.message = message

    def __str__(self):
        """Возвращает понятный текст ошибки."""
        return (
            f"BadCustomerError: customer: {self.customer}, "
            f"message: {self.message}"
        )


class BadProductError(Exception):
    """Ошибка для неверного названия товара."""

    def __init__(self, product, message):
        """Сохраняет название товара и сообщение об ошибке."""
        self.product = product
        self.message = message

    def __str__(self):
        """Возвращает понятный текст ошибки."""
        return (
            f"BadProductError: product: {self.product}, "
            f"message: {self.message}"
        )


class BadQuantityError(Exception):
    """Ошибка для неверного количества товара."""

    def __init__(self, quantity, message):
        """Сохраняет количество и сообщение об ошибке."""
        self.quantity = quantity
        self.message = message

    def __str__(self):
        """Возвращает понятный текст ошибки."""
        return (
            f"BadQuantityError: quantity: {self.quantity}, "
            f"message: {self.message}"
        )


class Order:
    """Класс одного заказа."""

    def __init__(self, order_id, customer, product, quantity, status="new"):
        """Создает заказ и сохраняет его основные данные."""
        self.order_id = order_id
        self.customer = customer
        self.product = product
        self.quantity = quantity
        self.status = status

    def __str__(self):
        """Возвращает заказ в удобном для пользователя виде."""
        return (
            f"id: {self.order_id} | customer: {self.customer} | "
            f"product: {self.product} | quantity: {self.quantity} | "
            f"status: {self.status}"
        )

    def to_dict(self):
        """Преобразует заказ в словарь."""
        return {
            "id": self.order_id,
            "customer": self.customer,
            "product": self.product,
            "quantity": self.quantity,
            "status": self.status,
        }


class OrderList:
    """Класс для хранения заказов и работы с ними."""

    __auto_id = 1

    def __init__(self):
        """Создает пустое хранилище заказов."""
        self.__orders = {}

    @classmethod
    def get_id(cls):
        """Возвращает новый ID заказа и увеличивает счетчик."""
        order_id = cls.__auto_id
        cls.__auto_id += 1
        return order_id

    @classmethod
    def reset_id(cls):
        """Сбрасывает счетчик ID. Используется в тестах."""
        cls.__auto_id = 1

    @staticmethod
    def status_is_valid(status):
        """Проверяет, является ли статус допустимым."""
        statuses = ["new", "processing", "done", "cancelled"]
        return status in statuses

    def create(self, customer, product, quantity):
        """Создает новый заказ и добавляет его в хранилище."""
        if len(customer) < 3:
            raise BadCustomerError(
                customer,
                "Имя клиента должно быть не короче 3 символов",
            )

        if len(product) < 3:
            raise BadProductError(
                product,
                "Название товара должно быть не короче 3 символов",
            )

        if quantity < 1 or quantity > 1000:
            raise BadQuantityError(
                quantity,
                "Количество должно быть в диапазоне от 1 до 1000",
            )

        order_id = OrderList.get_id()
        order = Order(order_id, customer, product, quantity)
        self.__orders[order_id] = order
        return order_id

    def read(self, order_id):
        """Возвращает заказ по его ID."""
        self.__check_id(order_id)

        if order_id not in self.__orders:
            raise BadIdError(order_id, "Заказ не существует")

        return self.__orders[order_id]

    def read_all(self):
        """Возвращает строку со всеми заказами."""
        if len(self.__orders) == 0:
            return "Список заказов пуст"

        result = ""
        for order in self.__orders.values():
            result += f"{order}\n"

        return result.rstrip()

    def update(self, order_id, customer, product, quantity):
        """Обновляет данные существующего заказа."""
        self.__check_id(order_id)

        if order_id not in self.__orders:
            raise BadIdError(order_id, "Заказ не существует")

        if len(customer) < 3:
            raise BadCustomerError(
                customer,
                "Имя клиента должно быть не короче 3 символов",
            )

        if len(product) < 3:
            raise BadProductError(
                product,
                "Название товара должно быть не короче 3 символов",
            )

        if quantity < 1 or quantity > 1000:
            raise BadQuantityError(
                quantity,
                "Количество должно быть в диапазоне от 1 до 1000",
            )

        order = self.__orders[order_id]
        order.customer = customer
        order.product = product
        order.quantity = quantity
        return True

    def update_status(self, order_id, status):
        """Изменяет статус существующего заказа."""
        order = self.read(order_id)

        if not OrderList.status_is_valid(status):
            raise ValueError(
                "Статус: new, processing, done или cancelled"
            )

        order.status = status
        return True

    def delete(self, order_id):
        """Удаляет заказ по ID."""
        self.__check_id(order_id)

        if order_id not in self.__orders:
            raise BadIdError(order_id, "Заказ не существует")

        del self.__orders[order_id]
        return True

    def export_csv(self, file_name):
        """Экспортирует все заказы в CSV файл."""
        with open(file_name, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(
                ["id", "customer", "product", "quantity", "status"]
            )

            for order in self.__orders.values():
                writer.writerow(
                    [
                        order.order_id,
                        order.customer,
                        order.product,
                        order.quantity,
                        order.status,
                    ]
                )

        return True

    def export_json(self, file_name):
        """Экспортирует все заказы в JSON файл."""
        data = []

        for order in self.__orders.values():
            data.append(order.to_dict())

        with open(file_name, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        return True

    def export_xml(self, file_name):
        """Экспортирует все заказы в XML файл."""
        root = ET.Element("orders")

        for order in self.__orders.values():
            order_element = ET.SubElement(root, "order")
            order_element.set("id", str(order.order_id))

            customer = ET.SubElement(order_element, "customer")
            customer.text = order.customer

            product = ET.SubElement(order_element, "product")
            product.text = order.product

            quantity = ET.SubElement(order_element, "quantity")
            quantity.text = str(order.quantity)

            status = ET.SubElement(order_element, "status")
            status.text = order.status

        tree = ET.ElementTree(root)
        tree.write(file_name, encoding="utf-8", xml_declaration=True)
        return True

    def __check_id(self, order_id):
        """Проверяет, находится ли ID в разрешенном диапазоне."""
        if order_id < 1 or order_id > 1000000:
            raise BadIdError(
                order_id,
                "ID должен быть в диапазоне от 1 до 1000000",
            )


class App:
    """Консольное приложение для работы с заказами."""

    def __init__(self, order_list):
        """Сохраняет объект списка заказов."""
        self.order_list = order_list

    @staticmethod
    def display_menu():
        """Возвращает текст главного меню."""
        return """
ORDER APP

1 - создать заказ
2 - показать заказ по ID
3 - показать все заказы
4 - обновить заказ
5 - изменить статус
6 - удалить заказ
7 - экспортировать заказы
0 - выход
"""

    def run(self):
        """Запускает главное меню приложения."""
        command = ""

        while command != "0":
            print(App.display_menu())
            command = input("Выберите действие: ")

            try:
                if command == "1":
                    customer = input("Имя клиента: ")
                    product = input("Название товара: ")
                    quantity = int(input("Количество: "))

                    order_id = self.order_list.create(
                        customer,
                        product,
                        quantity,
                    )
                    print("Заказ создан. ID:", order_id)

                elif command == "2":
                    order_id = int(input("ID заказа: "))
                    print(self.order_list.read(order_id))

                elif command == "3":
                    print(self.order_list.read_all())

                elif command == "4":
                    order_id = int(input("ID заказа: "))
                    customer = input("Новое имя клиента: ")
                    product = input("Новое название товара: ")
                    quantity = int(input("Новое количество: "))

                    self.order_list.update(
                        order_id,
                        customer,
                        product,
                        quantity,
                    )
                    print("Заказ обновлен")

                elif command == "5":
                    order_id = int(input("ID заказа: "))
                    status = input(
                        "Статус new/processing/done/cancelled: "
                    )
                    self.order_list.update_status(order_id, status)
                    print("Статус изменен")

                elif command == "6":
                    order_id = int(input("ID заказа: "))
                    self.order_list.delete(order_id)
                    print("Заказ удален")

                elif command == "7":
                    self.order_list.export_csv("exported_orders.csv")
                    self.order_list.export_json("exported_orders.json")
                    self.order_list.export_xml("exported_orders.xml")
                    print("Экспорт выполнен")

                elif command == "0":
                    print("До свидания")

                else:
                    print("Неизвестная команда")

            except (
                BadIdError,
                BadCustomerError,
                BadProductError,
                BadQuantityError,
                ValueError,
            ) as error:
                print("Ошибка:", error)
