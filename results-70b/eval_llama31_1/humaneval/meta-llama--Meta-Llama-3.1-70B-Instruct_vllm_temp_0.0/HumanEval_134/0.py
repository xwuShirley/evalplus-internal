def check_if_last_char_is_a_letter(txt):
    if not txt:
        return False
    words = txt.split()
    last_word = words[-1]
    last_char = last_word[-1]
    return len(last_word) == 1 and last_char.isalpha()