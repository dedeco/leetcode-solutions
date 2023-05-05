from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        p1 = p2 = 0
        while p1 < len(nums):
            if nums[p1] == 0:
                p2 = p1 + 1
                while p2 < len(nums) and nums[p2] == 0:
                    p2 += 1
                if p2 == len(nums):
                    break
                nums[p1], nums[p2] = nums[p2], nums[p1]
            p1 += 1


if __name__ == "__main__":
    Solution().moveZeroes(
        [0, 1, 0, 3, 12]
    )
