from typing import List


def binary_search(arr: List[int], low: int, high: int, x: int):
    if high >= low:
        mid = low + (high - low) // 2
        print(mid)
        if arr[mid] == x:
            return mid
        elif x > arr[mid]:
            return binary_search(arr, mid + 1, high, x)
        else:
            return binary_search(arr, low, mid - 1, x)
    else:
        return -1


if __name__ == "__main__":
    # driver code
    arr = [1, 5, 7, 10, 15, 110, 130]
    print("The position is {}".format(binary_search(
        arr, 0, len(arr)-1, 130
    )))
