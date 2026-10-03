import pytest

from textutils import snake_case


def test_simple():
    assert snake_case("Hello World") == "hello_world"


def test_multiple_spaces():
    assert snake_case("Hello    World") == "hello_world"


def test_leading_and_trailing_whitespace():
    assert snake_case("  Hello Open Source  ") == "hello_open_source"


def test_tabs_and_newlines():
    assert snake_case("Hello\tWorld\nAgain") == "hello_world_again"


def test_single_word():
    assert snake_case("Hello") == "hello"


def test_empty_string():
    assert snake_case("") == ""


def test_only_whitespace():
    assert snake_case("   ") == ""


def test_already_snake_case():
    assert snake_case("hello_world") == "hello_world"


def test_non_string_raises():
    with pytest.raises(TypeError):
        snake_case(42)