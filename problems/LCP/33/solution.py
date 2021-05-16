import solution
import heapq


class Solution(solution.Solution):
    def solve(self, test_input=None):
        bucket, vat = test_input
        return self.storeWater(list(bucket), list(vat))

    def storeWater(self, bucket, vat):
        """
        :type bucket: List[int]
        :type vat: List[int]
        :rtype: int
        """
        c = 0
        pq = []
        for i in range(len(bucket)):
            # 忽略掉不需要倒水的
            if not vat[i]:
                continue
            # bucket[i]为0时必须升级一次才能入队
            if not bucket[i]:
                bucket[i] += 1
                c += 1
            heapq.heappush(pq, (-vat[i]//bucket[i], i))
        # 不需要倒水
        if not pq:
            return 0
        # 当队列头部拥有众多需要相同倒水次数的组合时，就算只减少了最头部的组合的倒水数，
        # 也不会改善所需要的最大倒水次数(木桶效应)，在局部情况还会导致操作总次数增大
        # 应该综合考虑队列头部拥有众多需要相同倒水次数的组合
        # 看看给这些组合各增加一次容量能否使总操作数减少
        ans = 0
        # 当前需要的倾倒数
        cur = -pq[0][0]
        while pq[0][0] < -1:
            cur = -pq[0][0]
            # 想要提高最大倾倒数需要的升级数
            update = 0
            # 所有倾倒数为当前倾倒数的全部需要升级才能得到新的倾倒数
            while pq[0][0] == -cur:
                _, i = heapq.heappop(pq)
                update += 1
                bucket[i] += 1
                heapq.heappush(pq, (-vat[i] // bucket[i], i))
            # 如果新的倾倒数+升级需要的操作都比当前倾倒数小的话，那么升级的操作全部执行
            if cur >= -pq[0][0] + update:
                ans += update
            else:
                break
        return ans + cur + c

        # # 暴力遍历所有倾倒次数
        # ans, c, m = float("inf"), 0, 0
        # for i in range(len(bucket)):
        #     if not vat[i]:
        #         continue
        #     if not bucket[i]:
        #         bucket[i] += 1
        #         c += 1
        #     m = max(math.ceil(vat[i] / bucket[i]), m)
        # for i in range(1, m + 1):
        #     cur = i
        #     for j in range(len(bucket)):
        #         if not vat[j]:
        #             continue
        #         need = math.ceil(vat[j] / i)
        #         if bucket[j] < need:
        #             cur += need - bucket[j]
        #     ans = min(ans, cur)
        # if ans == float("inf"):
        #     return 0
        # return ans + c
