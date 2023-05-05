from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0
        high = len(numbers) - 1
        while low < high:
            sum_ = numbers[low] + numbers[high]
            if sum_ == target:
                return [low + 1, high + 1]
            elif sum_ < target:
                low += 1
            else:
                high -= 1

        return [1, 2]


# [2,7,11,15],
# 2
#   7 11
if __name__ == "__main__":
    output = Solution().twoSum(
        [-1, 0],
        -1
    )

    assert [1, 2] == output

    output = Solution().twoSum(
        [2, 7, 11, 15],
        9
    )

    assert [1, 2] == output

    output = Solution().twoSum(
        [-3, 3, 4, 90],
        0
    )

    assert [1, 2] == output

    output = Solution().twoSum(
        [2, 3, 4],
        6
    )

    assert [1, 3] == output
