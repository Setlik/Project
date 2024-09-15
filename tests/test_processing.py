from processing import filter_by_state, sort_by_date


def test_filter_by_state(filter_state_EXECUTED, filter_state_CANCELED, my_list):
    assert filter_by_state(my_list) == filter_state_EXECUTED
    assert filter_by_state(my_list,"CANCELED") == filter_state_CANCELED


def test_sort_by_date(sort_date, my_list):
    assert sort_by_date(my_list) == sort_date