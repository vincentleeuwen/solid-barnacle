import string


def rotate(text, key):
    ciphers = []
    for char in text:
        if char.isupper():
            ciphers.append(rotate_char(char, key, string.ascii_uppercase))
        elif char.islower():
            ciphers.append(rotate_char(char, key, string.ascii_lowercase))
        else:
            ciphers.append(char)
    return ''.join(ciphers)


def rotate_char(char, key, letters):
    next_index = letters.index(char) + key
    if next_index >= 26:
        next_index -= 26
    return letters[next_index]
