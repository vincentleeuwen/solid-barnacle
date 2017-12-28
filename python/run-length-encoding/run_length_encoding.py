import re


def decode(string):
    decoded = []
    number = 1
    for char in re.findall('\d+|\w|\s', string):
        try:
            number = int(char)
        except ValueError:
            decoded.append('{}'.format(number * char))
            number = 1
    return ''.join(decoded)


def encode(string):
    encoded = []
    counter = 1
    for char in string:
        if encoded and encoded[-1] == char:
            counter += 1
            if counter == 2:
                encoded.insert(-1, str(counter))
            else:
                encoded[-2] = str(counter)
        else:
            encoded.append(char)
            counter = 1
    return ''.join(encoded)
