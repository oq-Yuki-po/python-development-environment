from sample import calc


def test_calc():
    num_1 = 3
    num_2 = 5

    assert calc(num_1, num_2) == num_1 + num_2
