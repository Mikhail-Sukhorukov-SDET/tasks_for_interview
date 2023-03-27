import random


def sorting_example(numbers: list) -> list:
    pass

numbers_ex = list(range(100))
random.shuffle(numbers_ex)
assert sorting_example(numbers_ex) == list(range(100))
