from typing import List


def binary_search(arr: List[int], x: int):
    low = 0
    high = len(arr)-1
    while high >= low:
        mid = low + (high -1) // 2
        if arr[mid] == x:
            return mid
        elif x > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    else:
        return -1


if __name__ == "__main__":
    # driver code
    arr = [1, 5, 7, 10, 15, 110, 130]
    print("The position is {}".format(binary_search(
        arr, 15
    )))
