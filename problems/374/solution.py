import solution

NUM = 1


class Solution(solution.Solution):
    def solve(self, test_input=None):
        n, pick = test_input
        global NUM
        NUM = pick
        return self.guessNumber(n)

    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            ans = guess(mid)
            if ans == -1:
                right = mid - 1
            elif ans == 1:
                left = mid + 1
            else:
                return mid
        return left


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num):
    if num == NUM:
        return 0
    elif num > NUM:
        return -1
    return 1
