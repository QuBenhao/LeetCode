from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[[50, 1], [10, 8]], 5], Output=55.0))
		self.testcases.append(case(Input=[[[100, 30]], 50], Output=-1.0))

	def get_testcases(self):
		return self.testcases
