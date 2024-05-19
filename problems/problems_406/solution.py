import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.reconstructQueue(test_input)

    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        reorder = []
        list.sort(people, key=lambda x: (-x[0], x[1]))
        while people:
            person = people.pop(0)
            reorder.insert(person[1], person)
        return reorder
