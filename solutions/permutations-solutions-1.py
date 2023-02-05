"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]


Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""
from typing import List
import numpy


class Solution:

    def __init__(self):
        self.result = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.permute_numbers(nums, 0)
        return self.result

    def permute_numbers(self, nums: List[int], i: int):
        if i == len(nums):
            self.result.append(nums[:])
        for j in range(i, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            self.permute_numbers(nums, i + 1)
            nums[i], nums[j] = nums[j], nums[i]


# driver code
if __name__ == "__main__":
    arr = [1, 2, 3]
    output = Solution().permute(arr)
    numpy.testing.assert_array_equal(
        output,
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]
    )
