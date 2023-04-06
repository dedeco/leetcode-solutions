# 4,0,0,0,0 -> 4,0,0,0,0 // nothing to be done
# 0,0,2,0,0 -> 2,0,0,0,0 // 2 is left shifted
# 0,2,0,2,0 -> 4,0,0,0,0 // both '2' are left shifted and joined to form '4'
# 4,0,4,0,4 -> 8,4,0,0,0 // all three '4' are left shifted but only the first two are joined to form '8'
# 4,0,4,0,8 -> 8,8,0,0,0 // like the previous example, note the two '8' do not recursively combine.
from typing import List


class Solution:
    def shift_to_left(self, arr: List[int]):
        nums = []
        for n in arr:
            if n != 0:
                nums.append(n)

        j = 0
        temp = []
        while j < len(nums) - 1:
            if nums[j] == nums[j + 1]:
                temp.append(
                    nums[j] + nums[j + 1]
                )
                j += 1
            else:
                temp.append(nums[j])
            j += 1

        if j < len(nums):
            temp.append(nums[j])

        while len(temp) < len(arr):
            temp.append(0)

        return temp


if __name__ == "__main__":
    rows = [[4, 0, 0, 0, 0],
            [0, 0, 2, 0, 0],
            [0, 2, 0, 2, 0],
            [4, 0, 4, 0, 4],
            [4, 0, 4, 0, 8]]

    for r in rows:
        print(
            Solution().shift_to_left(
                r
            )
        )
