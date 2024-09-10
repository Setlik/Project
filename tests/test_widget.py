import pytest

from widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "value , expected",
    [
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("", ""),
    ],
)
def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected