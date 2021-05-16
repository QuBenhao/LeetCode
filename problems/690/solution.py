import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        list_employees, emp_id = test_input
        employees = []
        for id, importance, subordinates in list_employees:
            employees.append(Employee(id, importance, subordinates))
        return self.getImportance(employees, emp_id)

    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        employees_dict = {employee.id: employee for employee in employees}

        # def bfs(emps):
        #     if not emps:
        #         return 0
        #     new = []
        #     res = 0
        #     for employee in emps:
        #         res += employee.importance
        #         new += [employees_dict[emp_id] for emp_id in employee.subordinates]
        #     return res + bfs(new)
        #
        # return bfs([employees_dict[id]])

        def dfs(employee_id):
            employee = employees_dict[employee_id]
            return employee.importance + sum(dfs(emp_id) for emp_id in employee.subordinates)

        return dfs(id)


# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
        """
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        """
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
