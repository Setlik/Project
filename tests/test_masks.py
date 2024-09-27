from masks import get_mask_account, get_mask_card_number



def test_get_mask_card_number(numbers, empty):
    assert get_mask_card_number("7000792289606361") == numbers
    assert get_mask_card_number("") == empty
    assert get_mask_card_number("17000792289606361") == "1700 07** **** 6361"


def test_get_mask_account(accounts, empty):
    assert get_mask_account("73654108430135874305") == accounts
    assert get_mask_account("173654108430135874305") == accounts
    assert get_mask_account("") == empty