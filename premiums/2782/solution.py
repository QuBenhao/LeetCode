import solution
from typing import *


class CategoryHandler:
    def haveSameCategory(self, a: int, b: int) -> bool:
        pass

# Definition for a category handler.
class Solution(solution.Solution):
    def solve(self, test_input=None):
        n, categoryHandler = test_input
        return self.numberOfCategories(n, categoryHandler)

    def numberOfCategories(self, n: int, categoryHandler: Optional['CategoryHandler']) -> int:
            pass
        