def reverse(text: str) -> str:
    """Reverse a text.

    Args:
        text: The input text.

    Returns:
        The characters of ``text`` in reverse order.

    Example:
        >>> reverse("abc")
        'cba'
    """
    return text[::-1]