from typing import List


def find_pivot(arr: List, low: int, high: int):
    if arr[low] < arr[high]:
        return 0
    while low <= high:
        pivot = low + high // 2
        if arr[pivot] > arr[pivot + 1]:
            return pivot + 1
        else:
            if arr[pivot] < arr[low]:
                high = pivot - 1
            else:
                low = pivot + 1


if __name__ == "__main__":
    # driver code
    arr = [4, 5, 6, 7, 0, 1, 2, 3]
    print("The position is {}".format(
        find_pivot(arr, low=0, high=len(arr) - 1)
    )
    )
