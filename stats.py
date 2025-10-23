def word_count(text):
    return len(text.split())

def char_count(text):
    """Return a dict mapping each lowercase character (including symbols and spaces) to its count."""
    text = text.lower()
    counts = {}
    for ch in text:
        counts[ch] = counts.get(ch, 0) + 1
    return counts