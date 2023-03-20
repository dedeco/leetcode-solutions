import math
from typing import List


def jump_search(arr: List, target: int):
    n = len(arr)
    step = int(math.sqrt(len(arr)))
    prev = 0
    while arr[min([step, n])-1] < target:
        prev = step
        step += step
        if prev >= n:
            return -1
    while arr[prev] < target:
        prev += 1
        if prev == min([step, n]):
            return -1
    if arr[prev] == target:
        return prev
    return -1


if __name__ == "__main__":
    # driver code
    arr = [1, 5, 7, 10, 15, 110, 130]
    print("The position is {}".format(
        jump_search(arr, 15)
    ))
