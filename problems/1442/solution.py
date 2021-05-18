import solution
from collections import Counter


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countTriplets(list(test_input))

    def countTriplets(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # hashmap = defaultdict(list)
        # ans = 0
        # for j, num in enumerate(arr):
        #     new = defaultdict(list)
        #     for key, val in hashmap.items():
        #         # 如果hashmap中存在与当前num相等的key，那么他们的异或为0，
        #         # 他们之前的任意一个除最左边外的坐标作为右边都满足条件
        #         if key == num:
        #             ans += j * len(val) - sum(val)
        #         new[num ^ key] = val
        #     new[num].append(j)
        #     hashmap = new
        # return ans

        l, s = Counter(), Counter()
        prexor = ans = 0
        for k, num in enumerate(arr):
            # 将之前的异或结果更新
            l[prexor] += 1
            s[prexor] += k
            # curxor = arr[0] ^ arr[1] ^ ... ^ arr[k]
            prexor ^= num
            # 之前存在任意的i满足：arr[0] ^ arr[1] ^ ... ^ arr[i] = curxor,
            # 那么i到k可以构成一个异或为0的解，他们之前任意一个坐标(除i以为可以作为j)
            if prexor in l:
                # 同上面的双重循环解法, 利用数量和坐标距离更新
                ans += k * l[prexor] - s[prexor]
        return ans
