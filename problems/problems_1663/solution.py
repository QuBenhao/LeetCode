import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.getSmallestString(*test_input)

    def getSmallestString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        import string
        left = (26 * n - k) // 25
        mid = (k - left) % 26
        right = (k - left) // 26
        if mid == 0:
            right -= 1
        return 'a' * left + list(string.ascii_lowercase)[mid - 1] + 'z' * right

        # import string
        # ans = ""
        # for i in range(1, n + 1):
        #     if k - i <= 26 * (n - i):
        #         ans += "a"
        #     else:
        #         break
        # back = ""
        # k -= len(ans)
        # while k >= 26:
        #     back += 'z'
        #     k -= 26
        # if k > 0:
        #     back += list(string.ascii_lowercase)[k - 1]
        # return ans + back[::-1]
