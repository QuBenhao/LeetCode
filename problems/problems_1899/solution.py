import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.mergeTriplets(*test_input)

    def mergeTriplets(self, triplets, target):
        """
        :type triplets: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        x,y,z = target
        x_ = y_ = z_ = False
        for a,b,c in list(triplets):
            if a > x or b > y or c > z:
                continue
            if a == x:
                x_ = True
            if b == y:
                y_ = True
            if c == z:
                z_ = True
        return x_ and y_ and z_
