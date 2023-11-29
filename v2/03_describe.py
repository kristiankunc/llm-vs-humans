# Description: Describe what this code does and how it works. Do not go into full detail, just a brief description so that someone else can understand what it does without having to read the code. Test functions have their output commented after the function call.

from typing import List


def difference(arr: List[int], start: int, end: int) -> int:
    res = 0

    for i in range(start, end + 1):
        res += arr[i]

    for i in range(start):
        res -= arr[i]
    
    for i in range(end + 1, len(arr)):
        res -= arr[i]

    return res

# Tests
print(difference([1, 2, 3, 4, 5], 1, 3)) # 3
print(difference([1, 2, 3, 4, 5], 0, 3)) # 5