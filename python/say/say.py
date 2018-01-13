def say(number):
    numbers = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety'
    }
    k = 1000
    m = k * 1000
    b = m * 1000
    t = b * 1000

    if number >= 10 ** 12:
        raise ValueError('Number to big')
    if number < 0:
        raise ValueError('No negative number')

    if number < 20:
        return numbers[number]

    if number < 100:
        if number % 10 == 0:
            return numbers[number]
        else:
            return numbers[number // 10 * 10] + '-' + numbers[number % 10]

    if (number < k):
        if number % 100 == 0:
            return numbers[number // 100] + ' hundred'
        else:
            return numbers[number // 100] + ' hundred and ' + say(number % 100)

    if (number < m):
        if number % k == 0:
            return say(number // k) + ' thousand'
        elif number % k < 99:
            return say(number // m) + ' thousand and ' + say(number % k)
        else:
            return say(number // k) + ' thousand ' + say(number % k)

    if (number < b):
        if number % m == 0:
            return say(number // m) + ' million'
        elif number % m < 99:
            return say(number // m) + ' million and ' + say(number % m)
        else:
            return say(number // m) + ' million ' + say(number % m)

    if (number < t):
        if number % b == 0:
            return say(number // b) + ' billion'
        elif number % b < 99:
            return say(number // b) + ' billion and ' + say(number % b)
        else:
            return say(number // b) + ' billion ' + say(number % b)
