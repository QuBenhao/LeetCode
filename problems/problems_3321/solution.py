from collections import defaultdict

import solution
from typing import *
from sortedcontainers import SortedList


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findXSum(*test_input)

    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        cnt = defaultdict(int)
        L = SortedList()  # 保存 tuple (出现次数，元素值)
        R = SortedList()
        sum_l = 0  # L 的元素和

        def add(val: int) -> None:
            if cnt[val] == 0:
                return
            p = (cnt[val], val)
            if L and p > L[0]:  # p 比 L 中最小的还大
                nonlocal sum_l
                sum_l += p[0] * p[1]
                L.add(p)
            else:
                R.add(p)

        def remove(val: int) -> None:
            if cnt[val] == 0:
                return
            p = (cnt[val], val)
            if p in L:
                nonlocal sum_l
                sum_l -= p[0] * p[1]
                L.remove(p)
            else:
                R.remove(p)

        def l2r() -> None:
            nonlocal sum_l
            p = L[0]
            sum_l -= p[0] * p[1]
            L.remove(p)
            R.add(p)

        def r2l() -> None:
            nonlocal sum_l
            p = R[-1]
            sum_l += p[0] * p[1]
            R.remove(p)
            L.add(p)

        ans = [0] * (len(nums) - k + 1)
        for r, in_ in enumerate(nums):
            # 添加 in_
            remove(in_)
            cnt[in_] += 1
            add(in_)

            l = r + 1 - k
            if l < 0:
                continue

            # 维护大小
            while R and len(L) < x:
                r2l()
            while len(L) > x:
                l2r()
            ans[l] = sum_l

            # 移除 out
            out = nums[l]
            remove(out)
            cnt[out] -= 1
            add(out)
        return ans
