import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        S, K = test_input
        return self.decodeAtIndex(S, K)

    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        build_length = 0
        i = 0
        for c in S:
            if c.isdigit():
                build_length *= int(c)
            else:
                build_length += 1
                if build_length == K:
                    return c
            i += 1
            if build_length >= K:
                break
        for c in S[:i][::-1]:
            K %= build_length
            if K == 0 and not c.isdigit():
                return c
            if c.isdigit():
                build_length //= int(c)
            else:
                build_length -= 1
