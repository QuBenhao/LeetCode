import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        beginWord, endWord, wordList = test_input
        return self.ladderLength(beginWord, endWord, list(wordList))

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        import collections,string
        if beginWord not in wordList:
            wordList.append(beginWord)

        wordList = set(wordList)
        actions = collections.defaultdict(list)

        for s in wordList:
            for j in range(len(s)):
                for c in string.ascii_lowercase:
                    n = s[:j] + c + s[j+1:]
                    if n in wordList:
                        actions[s].append(n)

        frontier = [beginWord]
        explored = set()
        cost = 1

        while frontier:
            next_states = []
            for s in frontier:
                if s == endWord:
                    return cost
                explored.add(s)
                for n in actions[s]:
                    if n not in explored:
                        next_states.append(n)
            cost += 1
            frontier = next_states

        return 0
