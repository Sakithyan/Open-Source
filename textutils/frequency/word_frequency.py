import re
from collections import Counter


def word_frequency(text, top_n=None, min_length=1):
    """Count how many times each word appears in a text.

    Case-insensitive, punctuation ignored (except apostrophes and
    hyphens inside words). Accented letters are kept.

    Args:
        text: The input string.
        top_n: If given, return only the top_n most frequent words.
        min_length: Minimum word length to include in the result.

    Returns:
        A list of (word, count) tuples, sorted by count descending,
        then alphabetically for ties.

    Raises:
        TypeError: If text is not a string.
        ValueError: If top_n is negative or min_length is less than 1.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if top_n is not None and top_n < 0:
        raise ValueError("top_n must not be negative")
    if min_length < 1:
        raise ValueError("min_length must be at least 1")

    raw_words = text.split()
    words = []

    for word in raw_words:
        clean_word = re.sub(r"^[^\w'-]+|[^\w'-]+$", "", word)
        clean_word = clean_word.lower()
        if clean_word and len(clean_word) >= min_length:
            words.append(clean_word)

    counts = Counter(words)
    result = sorted(counts.items(), key=lambda pair: (-pair[1], pair[0]))

    if top_n is not None:
        result = result[:top_n]

    return result