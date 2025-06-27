import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.parseBoolExpr(test_input)

    def parseBoolExpr(self, expression: str) -> bool:
        ops, args = [], [[]]
        for c in expression:
            match c:
                case 't' | 'f':
                    args[-1].append(c == 't')
                case '&' | '|' | '!':
                    ops.append(c)
                case '(':
                    args.append([])
                case ')':
                    arguments = args.pop()
                    op = ops.pop()
                    match op:
                        case '&':
                            args[-1].append(all(arguments))
                        case '|':
                            args[-1].append(any(arguments))
                        case '!':
                            args[-1].append(not arguments[0])
                case _:
                    continue
        return args[0][0]
