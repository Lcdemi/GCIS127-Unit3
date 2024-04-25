import searches

def test_binary_search_mid():
    #setup
    a_list = [1, 3, 5, 7, 9, 11, 13]
    target = 7
    expected = 3

    #invoke
    actual = searches.binary_search(a_list, target)

    #analyze
    assert expected == actual

def test_binary_search_right():
    #setup
    a_list = [1, 3, 5, 7, 9, 11, 13]
    target = 11
    expected = 5

    #invoke
    actual = searches.binary_search(a_list, target)

    #analyze
    assert expected == actual

def test_binary_search_left():
    #setup
    a_list = [1, 3, 5, 7, 9, 11, 13]
    target = 3
    expected = 1

    #invoke
    actual = searches.binary_search(a_list, target)

    #analyze
    assert expected == actual

def test_binary_search_not_found():
    #setup
    a_list = [1, 3, 5, 7, 9, 11, 13]
    target = 8
    expected = None

    #invoke
    actual = searches.binary_search(a_list, target)

    #analyze
    assert expected == actual