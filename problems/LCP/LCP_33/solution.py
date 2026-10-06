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
            # Ignore vats that need no water
            if not vat[i]:
                continue
            # If bucket[i] is 0, upgrade it once before adding it to the queue
            if not bucket[i]:
                bucket[i] += 1
                c += 1
            heapq.heappush(pq, (-vat[i]//bucket[i], i))
        # No pouring is needed
        if not pq:
            return 0
        # When many bucket-vat pairs at the front of the queue require the same number of pours, reducing only the first pair's pour count
        # does not reduce the maximum pour count (the bottleneck), and may locally increase the total number of operations
        # Consider all pairs at the front of the queue that require the same number of pours together
        # Check whether increasing each bucket's capacity once reduces the total operation count
        ans = 0
        # Current number of pours required
        cur = -pq[0][0]
        while pq[0][0] < -1:
            cur = -pq[0][0]
            # Number of upgrades needed to improve the maximum pour count
            update = 0
            # Every pair at the current maximum pour count must be upgraded to obtain a lower pour count
            while pq[0][0] == -cur:
                _, i = heapq.heappop(pq)
                update += 1
                bucket[i] += 1
                heapq.heappush(pq, (-vat[i] // bucket[i], i))
            # Perform all upgrades if the new pour count plus upgrade operations is less than the current pour count
            if cur >= -pq[0][0] + update:
                ans += update
            else:
                break
        return ans + cur + c

        # # Brute-force all possible pour counts
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
