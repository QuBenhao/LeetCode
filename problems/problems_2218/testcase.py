from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[[1, 100, 3], [7, 8, 9]], 2], Output=101))
		self.testcases.append(case(Input=[[[100], [100], [100], [100], [100], [100], [1, 1, 1, 1, 1, 1, 700]], 7], Output=706))

	def get_testcases(self):
		return self.testcases
