import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.intToRoman(test_input)

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # # 打表法
        # ans = [['','M','MM','MMM'],
        #        ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM'],
        #        ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC'],
        #        ['','I','II','III','IV','V','VI','VII','VIII','IX']]
        # return "".join(ans[3-i][(num//(10**i))%10] for i in range(3,-1,-1))

        d = {1:'I', 5:'V', 10: 'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
        ans = []
        level = 1000
        while num:
            last = num//level
            if last == 4 or last == 9:
                ans.append(d[level])
                ans.append(d[(last + 1) * level])
            elif last > 4:
                ans.append(d[5 * level])
                for i in range(last-5):
                    ans.append(d[level])
            else:
                for i in range(last):
                    ans.append(d[level])
            num %= level
            level //= 10
        return "".join(ans)
