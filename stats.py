def word_count(text):
    return len(text.split())

def char_count(text):
    """Return a dict mapping each lowercase character (including symbols and spaces) to its count."""
    text = text.lower()
    counts = {}
    for ch in text:
        counts[ch] = counts.get(ch, 0) + 1
    return counts

def sort_on(items):
    """Convert a {char: num} dict into a list of {'char': c, 'num': n} dicts sorted by num desc."""
    lst = []
    for ch, num in items.items():
        lst.append({"char": ch, "num": num})
    def get_num(d):
        return d["num"]
    lst.sort(key=get_num, reverse=True)
    return lst
