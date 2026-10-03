import pytest

from textutils import capitalize_words


@pytest.mark.parametrize(
    "text, expected",
    [
        ("hello open source", "Hello Open Source"),
        ("hello", "Hello"),
        ("", ""),
        ("Hello World", "Hello World"),
        ("hELLO wORLD", "Hello World"),
        ("HELLO WORLD", "Hello World"),
        ("don't stop", "Don't Stop"),
        ("élève à l'école", "Élève À L'école"),
    ],
)
def test_capitalize_words(text, expected):
    assert capitalize_words(text) == expected


def test_capitalize_words_preserves_spacing():
    # Splitting on " " keeps repeated and surrounding spaces unchanged.
    assert capitalize_words("hello  world") == "Hello  World"
    assert capitalize_words(" hello ") == " Hello "