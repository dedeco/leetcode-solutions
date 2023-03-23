from typing import List


def binary_search(arr: List, low: int, high: int, x: int):
    while high >= low:
        mid = low + (high - low) // 2
        if arr[mid] == x:
            return mid
        elif x < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


# driver code
if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    print("The position is {}".format(binary_search(
        arr, 0, len(arr) - 1, 10
    )))
