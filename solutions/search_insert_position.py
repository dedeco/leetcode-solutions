"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

"""
from typing import List


class Solution:

    def binary_search(self, arr, low, high, x):
        while high >= low:
            mid = (low + high) // 2
            if arr[mid] == x:
                return mid
            elif x < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return low

    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, 0, len(nums) - 1, target)


# driver code
if __name__ == "__main__":
    arr =  [1,3,5,6]
    assert Solution().searchInsert(arr, 7) == 4
