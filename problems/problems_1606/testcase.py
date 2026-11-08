from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[3, [1, 2, 3, 4, 5], [5, 2, 3, 3, 3]], Output=[1]))
		self.testcases.append(case(Input=[3, [1, 2, 3, 4], [1, 2, 1, 2]], Output=[0]))
		self.testcases.append(case(Input=[3, [1, 2, 3], [10, 12, 11]], Output=[0, 1, 2]))

	def get_testcases(self):
		return self.testcases
