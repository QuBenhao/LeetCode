import solution
from typing import *
from collections import Counter


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumLength(test_input)

    def maximumLength(self, nums: List[int]) -> int:
        count = Counter(nums)
        max_len = 1  # 至少可以选一个元素

        # 特殊处理 x=1：因为 1^2 = 1，会形成全是 1 的序列
        # 序列长度必须是奇数（峰值 1 个，其余对称）
        if 1 in count:
            c = count[1]
            max_len = max(max_len, c if c % 2 == 1 else c - 1)

        for x in count:
            if x == 1:
                continue
            # 只有 count[x] >= 2 才能形成长度 > 1 的序列
            if count[x] < 2:
                continue

            # 构建链：每个数是前一个数的平方，且在数组中
            chain = [x]
            while chain[-1] ** 2 in count:
                chain.append(chain[-1] ** 2)

            # 找第一个 count < 2 的位置作为峰值
            # 默认峰值是链的最后一个
            peak_idx = len(chain) - 1
            for i, val in enumerate(chain):
                if count[val] < 2:
                    # count >= 1 可以作为峰值，count == 0 则峰值是前一个
                    peak_idx = i if count[val] >= 1 else i - 1
                    break

            if peak_idx >= 0:
                max_len = max(max_len, 2 * peak_idx + 1)

        return max_len

