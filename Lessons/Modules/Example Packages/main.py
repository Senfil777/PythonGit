from package_bank import stats as bs, logic as bl, exports as be


def main():
    bs.stat()
    bl.add(123)
    bl.change(321)
    bl.delete(453)
    bl.show()

    numbers = [1, 23, 4, 3, 3, 435, 34, 53]
    be.export(numbers)


if __name__ == "__main__":
    print("main.py was started")
    main()
