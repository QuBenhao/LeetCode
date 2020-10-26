class Solution(object):
    def tilingRectangle(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        if m == n:
            return 1
        if n > m:
            m,n = n,m
        
        return 0
