from typing import List

"""

k=3, n=7
1,2,3,... 9

 [1][2][3] = 7

"""


class Solution:

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        results = []

        def runner(remain, combs, next_start):
            if remain == 0 and len(combs) == k:
                results.append(combs.copy())
                return
            elif remain < 0 or len(combs) == k:
                return
            for i in range(next_start, 9):
                combs.append(i + 1)
                runner(remain - i - 1, combs, i + 1)
                combs.pop()

        runner(n, [], 0)

        return results


if __name__ == "__main__":
    print(Solution().combinationSum3(
        k=3,
        n=7
    ))
