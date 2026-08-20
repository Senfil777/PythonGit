class EmptyQueueError(Exception):
    """Ошибка: попытка получить элемент из пустой очереди."""

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"EmptyQueueError: message: {self.message}"


class Queue:
    """Простая очередь FIFO: First In - First Out."""

    def __init__(self):
        self.__queue = []

    def put(self, element):
        self.__queue.append(element)

    def get(self):
        if len(self.__queue) < 1:
            raise EmptyQueueError("Очередь пустая!")

        return self.__queue.pop(0)


def main():
    que = Queue()

    que.put(1)
    que.put("dog")
    que.put(False)

    try:
        for i in range(4):
            print(que.get())
    except EmptyQueueError:
        print("Queue error")


if __name__ == "__main__":
    main()
