import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minOperationsToFlip(str(test_input))

    def minOperationsToFlip(self, expression):
        """
        :type expression: str
        :rtype: int
        """
        """
        p1  op  p2  val, change
        0   |   0   0, min(c1,c2)
        0   |   1   1, 1
        1   |   0   1, 1
        1   |   1   1, min(c1,c2)+1
        0   &   0   0, min(c1,c2)+1
        0   &   1   0, 1
        1   &   0   0, 1
        1   &   1   1, min(c1,c2)
        """
        # l中没有括号，计算l的结果:val,change
        def cal(l):
            val, change = l[0]
            idx = 1
            while idx < len(l):
                op = l[idx]
                v, c = l[idx+1]
                if op == '|':
                    if val + v == 1:
                        val, change = 1, 1
                    elif not v:
                        val, change = 0, min(change, c)
                    else:
                        val, change = 1, min(change, c) + 1
                else:
                    if val + v == 1:
                        val, change = 0, 1
                    elif not v:
                        val, change = 0, min(change, c) + 1
                    else:
                        val, change = 1, min(change, c)
                idx += 2
            return val, change

        stack = [[]]
        for c in expression:
            if c == '(':
                stack.append([])
            elif c == ')':
                value, changes = cal(stack.pop())
                stack[-1].append((value,changes))
            elif c in '&|':
                stack[-1].append(c)
            else:
                # val, change for 0 or 1
                stack[-1].append((int(c),1))
        return cal(stack[0])[1]
