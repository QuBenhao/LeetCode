import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        ops = list(ops)
        inputs = list(inputs)
        # Your AuthenticationManager object will be instantiated and called as such:
        obj = AuthenticationManager(inputs[0][0])
        ans = [None]

        for i in range(1, len(ops)):
            if ops[i] == "renew":
                obj.renew(inputs[i][0], inputs[i][1])
                ans.append(None)
            elif ops[i] == "generate":
                obj.generate(inputs[i][0], inputs[i][1])
                ans.append(None)
            else:
                ans.append(obj.countUnexpiredTokens(inputs[i][0]))

        return ans


class AuthenticationManager(object):

    def __init__(self, timeToLive):
        """
        :type timeToLive: int
        """
        self.timeToLive = timeToLive
        self.tokens = dict()

    def generate(self, tokenId, currentTime):
        """
        :type tokenId: str
        :type currentTime: int
        :rtype: None
        """
        self.tokens[tokenId] = currentTime + self.timeToLive

    def renew(self, tokenId, currentTime):
        """
        :type tokenId: str
        :type currentTime: int
        :rtype: None
        """
        if tokenId in self.tokens and self.tokens[tokenId] > currentTime:
            self.tokens[tokenId] = currentTime + self.timeToLive

    def countUnexpiredTokens(self, currentTime):
        """
        :type currentTime: int
        :rtype: int
        """
        return sum(1 for key,val in self.tokens.items() if val > currentTime >= val - self.timeToLive)
