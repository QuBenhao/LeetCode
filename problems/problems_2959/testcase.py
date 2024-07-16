from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[3, 5, [[0, 1, 2], [1, 2, 10], [0, 2, 10]]], Output=5))
		self.testcases.append(case(Input=[3, 5, [[0, 1, 20], [0, 1, 10], [1, 2, 2], [0, 2, 2]]], Output=7))
		self.testcases.append(case(Input=[1, 10, []], Output=2))

	def get_testcases(self):
		return self.testcases
