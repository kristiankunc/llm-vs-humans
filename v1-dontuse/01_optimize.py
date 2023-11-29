# Description: Optimize this code to consistently run as fast as possible without changing the output.
import timeit


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# Tests
print(timeit.timeit("is_prime(95561)", globals=globals(), number=100))
