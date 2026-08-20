import configparser
import logging

from order_module import App, OrderList


def setup_logging(config):
    """Настраивает запись событий приложения в файл."""
    log_file = config["files"].get("log", "order_app.log")

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(levelname)s - %(message)s",
    )


def main():
    """Создает объекты приложения и запускает меню."""
    config = configparser.ConfigParser()
    config.read("settings.ini", encoding="utf-8")

    setup_logging(config)
    logging.info("Order application started")

    orders = OrderList()
    app = App(orders)
    app.run()

    logging.info("Order application finished")


if __name__ == "__main__":
    main()
