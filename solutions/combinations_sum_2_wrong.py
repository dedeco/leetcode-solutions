import copy
from typing import List


class Solution:

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        exists = {}

        if sum(candidates) < target:
            return []

        def runner(counts, combs, start):
            if sum(combs) == target:
                combs.sort()
                key = ''.join(map(lambda x: str(x), combs))
                if key not in exists:
                    exists[key] = 1
                    results.append(combs.copy())
                return
            elif sum(combs) > target:
                return
            for i in range(start, len(candidates)):
                if i == 0:
                    for k in candidates:
                        if k in counts:
                            counts[k] += 1
                        else:
                            counts[k] = 1
                if counts[candidates[i]] < 0:
                    continue
                combs.append(candidates[i])
                counts[candidates[i]] -= 1
                runner(copy.deepcopy(counts), combs, i + 1)
                counts[candidates[i]] += 1
                combs.pop()

        runner({}, [], 0)

        return results


if __name__ == "__main__":
    print(Solution().combinationSum2(
        [10, 1, 2, 7, 6, 1, 5],
        8
    ))

    print(Solution().combinationSum2(
        [4, 4, 2, 1, 4, 2, 2, 1, 3],
        6
    ))
