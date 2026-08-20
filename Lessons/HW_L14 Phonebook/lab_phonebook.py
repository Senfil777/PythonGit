import csv


class PhoneContact:
    """Класс одного контакта."""

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"Contact: {self.name}:{self.phone}"


class Phone:
    """Простая телефонная книга."""

    def __init__(self):
        self.contacts = []

    def show(self):
        """Показать все контакты."""
        print("Список контактов:")
        for contact in self.contacts:
            print(contact)

    def import_contacts_from_csv(self, file):
        """Импортировать контакты из CSV файла."""
        print("Импортирую контакты...")

        with open(file, newline="", encoding="utf-8") as csvfile:
            fieldnames = ["Name", "Phone"]
            reader = csv.DictReader(csvfile, fieldnames=fieldnames)

            for row in reader:
                contact = PhoneContact(row["Name"], row["Phone"])
                self.contacts.append(contact)

        print("Импорт был успешен...")

    def export_contacts_to_csv(self, file):
        """Экспортировать контакты в CSV файл."""
        print("Экспортирую контакты...")

        with open(file, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(
                csvfile,
                delimiter=",",
                quotechar='"',
                quoting=csv.QUOTE_MINIMAL
            )

            for contact in self.contacts:
                writer.writerow([contact.name, contact.phone])

        print("Экспорт был успешен...")

    def search_contacts(self):
        """Поиск контакта по имени или номеру телефона."""
        phrase = input("Search contacts: ")
        print("Поиск контакта по фразе:")

        count = 0

        for contact in self.contacts:
            if phrase.lower() in contact.name.lower() or phrase in contact.phone:
                print("Найден контакт:", contact)
                count += 1

        if count == 0:
            print("Контакт не найден!")


def main():
    phone = Phone()

    phone.import_contacts_from_csv("phone_book.csv")
    phone.show()
    phone.search_contacts()
    phone.export_contacts_to_csv("exported_phone_book.csv")


if __name__ == "__main__":
    main()
