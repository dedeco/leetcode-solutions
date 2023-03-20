"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1


Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 1:
            return 0 if nums[0] == target else -1
        first = self.find_pivot(nums, 0, n - 1) or 0
        if target == nums[first]:
            return first
        elif first == 0:
            return self.search_idx(nums, 0, len(nums) - 1, target)
        elif target > nums[first]:
            return self.search_idx(nums, 0, first, target)
        else:
            return self.search_idx(nums, first, len(nums) - 1, target)

    def find_pivot(self, arr: List, low: int, high: int):
        if arr[low] < arr[high]:
            return 0
        while low <= high:
            pivot = (low + high) // 2
            if arr[pivot] > arr[pivot + 1]:
                return pivot + 1
            else:
                if arr[pivot] < arr[low]:
                    high = pivot - 1
                else:
                    low = pivot + 1

    def search_idx(self, arr: List[int], low: int, high: int, target: int):
        while low <= high:
            pivot = (low + high) // 2
            if arr[pivot] == target:
                return pivot
            else:
                if target < arr[pivot]:
                    high = pivot - 1
                else:
                    low = pivot + 1
        return -1


# driver code
if __name__ == "__main__":
    arr = [5, 1, 3]
    assert Solution().search(arr, 3) == 2
