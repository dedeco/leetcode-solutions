from typing import List


def rotate(arr: List[int], i: int) -> List[int]:
    return arr[-i:] + arr[:-i]


if __name__ == "__main__":
    # driver code
    arr = [4, 5, 6, 7, 0, 1, 2, 3]
    print("New array {} ".format(
        rotate(arr, 4)
    )
    )
