# [Python] dict

> Author: Benhao
> Date: 2021-03-21
> Upvotes: 1
> Tags: Python

---

### 解题思路
此处撰写解题思路

### 代码

```python
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
        return sum(1 for key,val in self.tokens.items() if val > currentTime)

```