def binary_search(arr, low, high, x):
    if high >= low:
        mid = low + (high - low) // 2
        if arr[mid] == x:
            return mid
        elif x > arr[mid]:
            return binary_search(arr, mid + 1, high, x)
        else:
            return binary_search(arr, low, mid - 1, x)
    else:
        return -1


# driver code
if __name__ == "__main__":
    arr = [2, 3, 4, 10, 40]
    print("The position is {}".format(binary_search(
        arr, 0, len(arr)-1, 10
    )))
