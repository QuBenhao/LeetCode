import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.fullJustify(*test_input)

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, line, str_num = [], [], 0
        for word in words:
            # line中所有单词加一起的长度 + line中单词(单词与单词之间原生需要1个空格)之间的间距数 + 当前需要判断的单词长度
            # 上述之和大于等于maxWidth时会溢出，为什么等于时也会溢出？因为若新加入Word，会新增加1个间距(即空格长度)
            if str_num + len(line)-1 + len(word) >= maxWidth:
                for i in range(maxWidth - str_num):
                    line[i%max(len(line)-1, 1)] += ' '     #循环将每个空格依次加到每个单词之间的间距上
                res.append(''.join(line))
                line, str_num = [], 0         
            line.append(word)
            str_num += len(word)
        return res + [' '.join(line).ljust(maxWidth)]
