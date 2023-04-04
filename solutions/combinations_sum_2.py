from collections import defaultdict
from typing import List


class Solution:

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        results = []

        if sum(candidates) < target:
            return []

        def runner(combs, start, counter, remains):
            if remains == 0:
                results.append(combs.copy())
                return
            elif remains < 0:
                return

            for i in range(start, len(counter)):

                candidate, freq = counter[i]

                if freq <= 0:
                    continue

                combs.append(candidate)
                counter[i] = (candidate, freq - 1)

                runner(combs, i, counter, remains - candidate)

                counter[i] = (candidate, freq)
                combs.pop()

        counter = defaultdict(int)
        for x in candidates:
            counter[x] += 1
        t_counter = [(k, v) for k, v in counter.items()]

        runner([], 0, t_counter, target)

        return results


