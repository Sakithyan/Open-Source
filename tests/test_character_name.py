import pytest

from textutils import character_count


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Hello", 5),
        ("", 0),
        ("Hello World", 11),   # spaces are counted
        ("   ", 3),
        ("a\tb\n", 4),
        ("café", 4),
    ],
)
def test_character_count(text, expected):
    assert character_count(text) == expected