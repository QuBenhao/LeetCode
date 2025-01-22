from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[[0, 1], [1, 2], [2, 3]], [10, 10, 3, 3], 5], Output=11))
		self.testcases.append(case(Input=[[[0, 1], [0, 2]], [8, 4, 4], 0], Output=16))

	def get_testcases(self):
		return self.testcases
