import random


def evaluate_number(n: int):
    if n % 3 == 0 and n % 5 == 0:
        return "Gestform"
    elif n % 3 == 0:
        return "Geste"
    elif n % 5 == 0:
        return "Forme"
    else:
        return str(n)


def evaluate_list(integer_list: list):
    for n in integer_list:
        print(evaluate_number(n))


if __name__ == "__main__":
    BOUND_MIN = -1000
    BOUND_MAX = 1000
    LIST_COUNT = 12
    random_integer_list = random.sample(range(BOUND_MIN, BOUND_MAX), LIST_COUNT)
    print(random_integer_list)
    evaluate_list(random_integer_list)
