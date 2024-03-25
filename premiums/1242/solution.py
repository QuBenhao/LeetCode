import solution
from typing import *


# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
#class HtmlParser(object):
#    def getUrls(self, url):
#        :type url: str
#        :rtype List[str]

class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.crawl(*test_input)

    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
            pass
        