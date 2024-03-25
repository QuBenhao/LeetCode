from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[5, [[1, 3, 2], [2, 4, 3], [0, 2, -2]]], Output=[-2, 0, 3, 5, 3]))
		self.testcases.append(case(Input=[10, [[2, 4, 6], [5, 6, 8], [1, 9, -4]]], Output=[0, -4, 2, 2, 2, 4, 4, -4, -4, -4]))

	def get_testcases(self):
		return self.testcases
