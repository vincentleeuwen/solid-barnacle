import string


def encode(plain_text):
    encoded = []
    counter = 0
    for c in filter(str.isalnum, plain_text.lower()):
        if c.isalpha():
            counter += 1
            encoded.append(
                string.ascii_lowercase[::-1][string.ascii_lowercase.index(c)])
        elif c.isdigit():
            counter += 1
            encoded.append(c)
        if counter and counter % 5 == 0 and encoded[-1] != ' ':
            encoded.append(' ')
    return ''.join(encoded).strip()


def decode(ciphered_text):
    decoded = []
    for c in filter(str.isalnum, ciphered_text.lower()):
        if c.isalpha():
            decoded.append(
                string.ascii_lowercase[::-1][string.ascii_lowercase.index(c)])
        elif c.isdigit():
            decoded.append(c)
    return ''.join(decoded)
