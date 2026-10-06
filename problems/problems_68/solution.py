import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.fullJustify(*test_input)

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, line, str_num = [], [], 0
        for word in words:
            # Total length of words in line + number of gaps between them (each needs one space) + length of the word being considered
            # A sum greater than or equal to maxWidth overflows; equality also overflows because adding Word introduces one more gap (one space)
            if str_num + len(line)-1 + len(word) >= maxWidth:
                for i in range(maxWidth - str_num):
                    line[i%max(len(line)-1, 1)] += ' '     # Repeatedly add one space to each gap between words in turn
                res.append(''.join(line))
                line, str_num = [], 0         
            line.append(word)
            str_num += len(word)
        return res + [' '.join(line).ljust(maxWidth)]
