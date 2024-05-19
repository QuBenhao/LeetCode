from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[[1, 3], [6, 9]], [2, 5]], Output=[[1, 5], [6, 9]]))
		self.testcases.append(case(Input=[[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]], Output=[[1, 2], [3, 10], [12, 16]]))

	def get_testcases(self):
		return self.testcases
