from random import random
from time import time


def get_random_numbers(n, maxim=10 ** 6, mini=0):
    return [int(random() * maxim) for _ in range(n)]


def measure(fn):
    st = time()
    fn()
    print(time() - st)