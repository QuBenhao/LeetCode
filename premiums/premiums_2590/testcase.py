from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['TodoList', 'addTask', 'addTask', 'getAllTasks', 'getAllTasks', 'addTask', 'getTasksForTag', 'completeTask', 'completeTask', 'getTasksForTag', 'getAllTasks'], [[], [1, 'Task1', 50, []], [1, 'Task2', 100, ['P1']], [1], [5], [1, 'Task3', 30, ['P1']], [1, 'P1'], [5, 1], [1, 2], [1, 'P1'], [1]]], Output=[None, 1, 2, ['Task1', 'Task2'], [], 3, ['Task3', 'Task2'], None, None, ['Task3'], ['Task3', 'Task1']]))

	def get_testcases(self):
		return self.testcases
