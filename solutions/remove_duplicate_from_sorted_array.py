from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = j = 0
        while j < len(nums):
            j = i + 1
            while j < len(nums) and (nums[i] == nums[j] or nums[i] > nums[j]):
                j += 1
            if j >= len(nums):
                break
            nums[i + 1] = nums[j]
            i = i + 1
        return nums


if __name__ == "__main__":
    print(
        Solution().removeDuplicates(
            [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        ))
