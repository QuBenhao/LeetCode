import solution
import heapq
from collections import Counter


class Solution(solution.Solution):
    def solve(self, test_input=None):
        words, k = test_input
        return self.topKFrequent(list(words), k)

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