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