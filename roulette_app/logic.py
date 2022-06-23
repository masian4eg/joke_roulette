import random


def get_spins(array):
    if array:
        random_spin = random.randint(0, len(array) - 1)
        spin = array.pop(random_spin)
        return spin
    elif not array:
        return 11
