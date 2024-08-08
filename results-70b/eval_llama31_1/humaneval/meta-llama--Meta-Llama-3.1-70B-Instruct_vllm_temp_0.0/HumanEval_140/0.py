import re

def fix_spaces(text):
    text = re.sub(' +', lambda m: '_' if m.group(0).count(' ') <= 2 else '-', text)
    return text