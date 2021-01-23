import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        n, languages, friendships = test_input
        return self.minimumTeachings(n, [x[:] for x in languages], [x[:] for x in friendships])

    def minimumTeachings(self, n, languages, friendships):
        """
        :type n: int
        :type languages: List[List[int]]
        :type friendships: List[List[int]]
        :rtype: int
        """
        ans = len(languages)
        friends = []
        for a,b in friendships:
            if not set(languages[a-1]) & set(languages[b-1]):
                friends.append([a,b])
        for i in range(1,n+1):
            count = 0
            explored = set()
            for a,b in friends:
                if i in languages[a-1]:
                    if b not in explored:
                        count += 1
                elif i in languages[b-1] or b in explored:
                    if a not in explored:
                        count += 1
                elif a not in explored and b not in explored:
                    count += 2
                else:
                    count += 1
                explored.add(a)
                explored.add(b)
            if count < ans:
                ans = count
        return ans

        # languages = [set(l) for l in languages]
        #
        # dontspeak = set()
        # for u, v in friendships:
        #     u = u-1
        #     v = v-1
        #     if languages[u] & languages[v]: continue
        #     dontspeak.add(u)
        #     dontspeak.add(v)
        #
        # langcount = Counter()
        # for f in dontspeak:
        #     for l in languages[f]:
        #         langcount[l] += 1
        #
        # return 0 if not dontspeak else len(dontspeak) - max(list(langcount.values()))
