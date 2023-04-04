from typing import List

"""

Input: candidates = [2,3,6,7], target = 7



"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        results = []

        def runner(combs, start):
            if sum(combs) == target:
                results.append(combs.copy())
                return
            elif sum(combs) > target:
                return
            for i in range(start, len(candidates)):
                combs.append(candidates[i])
                runner(combs, i)
                combs.pop()
        runner([], 0)

        return results


if __name__ == "__main__":
    print(Solution().combinationSum(
        [2, 3, 6, 7],
        7
    ))
