import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        students, sandwiches = test_input
        return self.countStudents(students.copy(),sandwiches.copy())

    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        count = len(students)
        while sandwiches and students and sandwiches[0] in students:
            sandwich = sandwiches.pop(0)
            i = students.index(sandwich)
            students.pop(i)
            count -= 1
        return count
