import os
import random
import string
import time
import timeit
from statistics import mean
from statistics import stdev

token = os.getenv('paytoken')

alphabet = string.ascii_uppercase + string.digits
uid_length: int = 6

def random_choice():
    return ''.join(random.choices(alphabet, k=uid_length))
def random_choice_num():
    return ''.join(random.choices(string.digits, k=uid_length))

def test_collisions(function):
    out = set()
    count = 0
    for _ in range(100000):
        new = function()
        if new in out:
            count += 1
        else:
            out.add(new)
    return count


def run_and_print_results(function):
    round_digits = 5
    now = time.time()
    collisions = test_collisions(function)
    total_time = round(time.time() - now, round_digits)

    trials = 1_000
    runs = 100
    func_time = timeit.repeat(function, repeat=runs, number=trials)
    avg = round(mean(func_time), round_digits)
    std = round(stdev(func_time), round_digits)

    print(f'{function.__name__}: collisions {collisions} - '
          f'time (s) {avg} ± {std} - '
          f'total (s) {total_time}')

print(random_choice())
print(random_choice_num())

if __name__ == '__main__':
    run_and_print_results(random_choice)
