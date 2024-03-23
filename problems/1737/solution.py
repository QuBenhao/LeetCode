import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minCharacters(*test_input)

    def minCharacters(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        from collections import Counter
        import string

        l1, l2 = len(a), len(b)
        ans = l1 + l2
        adict = Counter()
        bdict = Counter()
        for c in a:
            adict[c] += 1
        for c in b:
            bdict[c] += 1

        # condition 3
        for k in adict:
            ans = min(ans, l1 + l2 - adict[k] - bdict[k])

        for le in list(string.ascii_lowercase):
            if le == 'a':
                continue

                # condition 1
            opa = 0
            for k in adict:
                if k >= le:
                    opa += adict[k]
            for k in bdict:
                if k < le:
                    opa += bdict[k]
            # condition2: l1 + l2 - opa
            ans = min(opa, l1 + l2 - opa, ans)

        return ans

        # m, n = len(a), len(b)
        # c1 = Counter(ord(c) - 97 for c in a)
        # c2 = Counter(ord(c) - 97 for c in b)
        # res = m + n - max((c1 + c2).values()) # condition 3
        # for i in range(25):
        #     c1[i + 1] += c1[i]
        #     c2[i + 1] += c2[i]
        #     res = min(res, m - c1[i] + c2[i]) # condition 1
        #     res = min(res, n - c2[i] + c1[i]) # condition 2
        # return res
