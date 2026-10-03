import pytest

from textutils import word_count


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Hello Open Source!", 3),
        ("Hello", 1),
        ("", 0),
        ("   ", 0),
        ("Hello    World", 2),
        ("  Hello World  ", 2),
        ("Hello\tWorld\nAgain", 3),
        ("open-source is great", 3),
    ],
)
def test_word_count(text, expected):
    assert word_count(text) == expected