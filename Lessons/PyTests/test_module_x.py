import module_x


def test_name_upper_not_str_false_int():
    assert module_x.name_upper(123) == False


def test_name_upper_not_str_false_list():
    assert module_x.name_upper([1, 2, 34]) == False


def test_name_upper_not_str_false_tuple():
    assert module_x.name_upper((1, 2, 3, 4)) == False


def test_name_upper_not_str_false_set():
    assert module_x.name_upper({1, 2, 3, 4}) == False


def test_name_upper_str_name_upper_stef():
    assert module_x.name_upper("stef") == "STEF"


def test_name_upper_str_name_upper_kat():
    assert module_x.name_upper("kat") == "KAT"


def test_name_upper_str_name_upper_dima():
    assert module_x.name_upper("dima") == "DIMA"