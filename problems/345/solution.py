import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.reverseVowels(str(test_input))

    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}
        lt = list(s)
        l, r = 0, len(s) - 1
        while l < r:
            if lt[l] in vowels and lt[r] in vowels:
                lt[l], lt[r] = lt[r], lt[l]
                l += 1
                r -= 1
            elif lt[l] in vowels:
                r -= 1
            else:
                l += 1
        return ''.join(lt)
