import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.strStr(*test_input)

    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # KMP Algorithm
        # txt: original , pat: pattern
        def KMP_preprocess(pat):
            i, length, n = 1, 0, len(pat)
            lps = [0] * n
            while i < n:
                if pat[i] == pat[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                elif length:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
            return lps

        def KMP_search(txt, pat):
            m, n = len(txt), len(pat)
            if not n:
                return 0
            lps = KMP_preprocess(pat)
            i = j = 0
            while i < m:
                if txt[i] == pat[j]:
                    i += 1
                    j += 1
                if j == n:
                    return i - j
                if i < m and txt[i] != pat[j]:
                    if j:
                        j = lps[j - 1]
                    else:
                        i += 1
            return -1

        return KMP_search(haystack, needle)
