import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.halvesAreAlike(str(test_input))

    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        cl = cr = 0
        for i,c in enumerate(s):
            if c in vowels:
                if i < len(s)//2:
                    cl += 1
                else:
                    cr += 1
        if cl == cr:
            return True
        return False
