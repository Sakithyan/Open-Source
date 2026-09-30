"""Text casing utilities."""


def capitalize_words(text: str) -> str:
    """Capitalize the first letter of every word in a text.

    Args:
        text: The input text.

    Returns:
        ``text`` with each word capitalized. Original spacing is preserved.

    Example:
        >>> capitalize_words("hello open source")
        'Hello Open Source'
    """
    return " ".join(word.capitalize() for word in text.split(" "))