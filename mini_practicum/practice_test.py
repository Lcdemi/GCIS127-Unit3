import practice

def test_absolute_difference_test_5_3():
    #setup
    a = 5
    b = 3
    expected = 2

    #invoke
    actual = practice.absolute_difference(a, b)

    #analyze
    assert actual == expected

def test_absolute_difference_test_5_5():
    #setup
    a = 5
    b = 5
    expected = 0

    #invoke
    actual = practice.absolute_difference(a, b)

    #analyze
    assert actual == expected

def test_absolute_difference_test_3_5():
    #setup
    a = 3
    b = 5
    expected = 2

    #invoke
    actual = practice.absolute_difference(a, b)

    #analyze
    assert actual == expected