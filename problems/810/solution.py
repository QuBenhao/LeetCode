import solution
from functools import reduce
from operator import xor


class Solution(solution.Solution):
    def solve(self, test_input):
        return self.xorGame(list(test_input))

    def xorGame(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """
        nums长度为偶数时，先手必胜
        反证法：假设无论Alice擦去哪个数，Bob都必胜
        由于数组长度为偶数，所以Bob获胜时不能是数全被擦光了（因为偶数个回合最后擦的肯定是Bob），肯定是存在某个回合，无论Alice擦掉哪个，异或都为0
        即n1 ^ n2 ^ ... nk = a (a!=0), n1 ^ n2 ^..^ nk-1 = n2 ^..^ nk = n1 ^ n3 ^.. ^ nk = 0
        上面的所有式子成立当且仅当 n1 = n2 = .. = nk = a 且 k为奇数
        那么必然是剩余奇数个a，相当于Alice擦的时候，数组长度为奇数，这nums长度为偶数是矛盾的
        
        那么如果nums长度为奇数时，Alice想赢，只能是nums异或结果本身为0
        这是因为无论Alice擦掉哪个数，数组长度都变为偶数且Bob先手，那么Bob就必胜
        """
        return len(nums) % 2 == 0 or reduce(xor, nums) == 0
