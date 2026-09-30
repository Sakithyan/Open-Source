"""Basic text transformation and counting utilities."""


def word_count(text: str) -> int:
    """Count the words in a text.

    Words are sequences of characters separated by whitespace.

    Args:
        text: The input text.

    Returns:
        The number of words in ``text``.

    Example:
        >>> word_count("Hello Open Source!")
        3
    """
    return len(text.split())


def character_count(text: str) -> int:
    """Count the characters in a text, including spaces and punctuation.

    Args:
        text: The input text.

    Returns:
        The number of characters in ``text``.

    Example:
        >>> character_count("Hello")
        5
    """
    return len(text)