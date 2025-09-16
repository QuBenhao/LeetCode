from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['NumberContainers', 'find', 'change', 'change', 'change', 'change', 'find', 'change', 'find'], [[], [10], [2, 10], [1, 10], [3, 10], [5, 10], [10], [1, 20], [10]]], Output=[None, -1, None, None, None, None, 1, None, 2]))

	def get_testcases(self):
		return self.testcases
