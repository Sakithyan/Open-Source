import pytest

from textutils import reverse


@pytest.mark.parametrize(
    "text, expected",
    [
        ("abc", "cba"),
        ("", ""),
        ("a", "a"),
        ("radar", "radar"),
        ("Hello World", "dlroW olleH"),
        ("  ab ", " ba  "),
    ],
)
def test_reverse(text, expected):
    assert reverse(text) == expected


def test_reverse_twice_returns_original():
    text = "Open Source"
    assert reverse(reverse(text)) == text