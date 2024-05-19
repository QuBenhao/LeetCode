import solution
import heapq
from collections import Counter


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.topKFrequent(*test_input)

    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        count = Counter(words)
        pq = []
        for key,val in count.items():
            heapq.heappush(pq, (-val, key))
        return [x[1] for x in heapq.nsmallest(k, pq)]