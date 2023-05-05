from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(n):
            nums1[i+m] = nums2[i]
        nums1.sort()
        return nums1


if __name__ == "__main__":
    print(Solution().merge(
        nums1=[1, 2, 3, 0, 0, 0],
        m=3,
        nums2=[2, 5, 6],
        n=3
    ))

    print(Solution().merge(
        nums1=[4, 5, 6, 0, 0, 0],
        m=3,
        nums2=[1, 2, 3],
        n=3
    ))
