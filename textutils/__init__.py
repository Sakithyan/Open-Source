"""textutils: a lightweight text-processing library."""

from .casing import capitalize_words
from .transform import character_count, reverse, word_count

__all__ = ["word_count", "character_count", "reverse", "capitalize_words"]