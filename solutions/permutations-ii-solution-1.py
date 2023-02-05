"""
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.



Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""

from typing import List

import numpy

from collections import defaultdict


class Solution:
    def __init__(self) -> None:
        self.output = defaultdict(int)

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.runner(nums)
        return self.convert(self.output)

    def convert(self, d: dict[str, int]) -> List[List[int]]:
        result = []
        for key in d.keys():
            nums = [int(c) for c in key]
            result.append(nums)
        return result

    def runner(self, nums: List[int], i: int = 0):
        if i == len(nums.copy()):
            key = tuple(nums.copy())
            self.output[key] += 1
        for j in range(i, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            self.runner(nums, i + 1)
            nums[i], nums[j] = nums[j], nums[i]


# driver code
if __name__ == "__main__":
    arr = [1, 1, 2]
    output = Solution().permuteUnique(arr)
    numpy.testing.assert_array_equal(
        output, [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
    )
