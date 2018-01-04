def is_armstrong(number):
    return number == sum([int(i)**len(str(number)) for i in str(number)])
