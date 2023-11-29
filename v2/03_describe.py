# Description: Describe what this code does and how it works. Do not go into full detail, just a brief description so that someone else can understand what it does without having to read the code.

from typing import List


def difference(arr: List[int], start: int, end: int) -> int:
    res = 0

    for i in range(start, end + 1):
        print(f"adding {i}")
        res += arr[i]

    for i in range(start):
        print(f"removing {i}")
        res -= arr[i]
    
    for i in range(end + 1, len(arr)):
        print(f"removing {i}")
        res -= arr[i]

    return res

# Tests
print(difference([1, 2, 3, 4, 5], 1, 3)) # 3
print(difference([1, 2, 3, 4, 5], 0, 3)) # 5