from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        for right in range(1, len(nums)):
            print(nums[right - 1], nums[right])
            if nums[right - 1] != nums[right]:
                nums[left] = nums[right]
                left += 1
        return left

"""
[0, 1, 2, 3, 1, 2, 2, 3, 3, 4]
          L  
                   R  R  
"""


if __name__ == "__main__":
    print(
        Solution().removeDuplicates(
            [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        ))
