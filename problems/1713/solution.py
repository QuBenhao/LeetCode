import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minOperations(*test_input)

    def minOperations(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: int
        """
        """
        Pre knowledge

        LCS (longest common sequence)
        LIS (longest increasing sequence)
        Solve LIS in O(nlogn) time
        
        
        Intuition
        
        Seems to be LCS problem,
        and we can easily solve in O(n^2),
        then it will get TLE.
        
        Actually there is a bold hint in the statement,
        "You are given an array target that consists of distinct integers"
        
        So there is an order for elements in the target.
        For element in A, if it's not in target, we ignore it.
        If it's in target, we want find the sequence ending with lower order.
        
        So we we actually want to find an increase sequence in the A.
        This a typical LIS problems.
        Just a small difference,
        we don't want it to be increase in the element's value,
        but in the element's order.
        
        
        Explanation
        
        Same as LIS problem.
        
        
        Complexity
        
        Time O(nlogn)
        Space O(n)
        """
        import bisect
        h = {a: i for i, a in enumerate(target)}
        stack = []
        for a in arr:
            if a not in h:
                continue
            i = bisect.bisect_left(stack, h[a])
            if i == len(stack):
                stack.append(0)
            stack[i] = h[a]
        return len(target) - len(stack)
