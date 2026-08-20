from mobile_phone_class import MobilePhone


def main():
    phone1 = MobilePhone("375290077000")
    phone2 = MobilePhone("375330011001")

    print(phone1.turn_on())
    print(phone2.turn_on())

    print(phone1.call("375291112233"))
    print(phone2.call("375292223344"))

    print(phone1.turn_off())
    print(phone2.turn_off())


if __name__ == "__main__":
    main()
