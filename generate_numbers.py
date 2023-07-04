import random


def generate_couple_of_numbers():
    suffix = random.randint(0, 9)
    suffix = str(suffix) + str(suffix)
    return suffix


def generate_phone_number():
    prefix = "+795551"
    suffix1 = generate_couple_of_numbers()
    suffix2 = generate_couple_of_numbers()
    suffix3 = generate_couple_of_numbers()
    suffix = suffix1 + suffix2 + suffix3
    number = prefix + suffix
    return number
