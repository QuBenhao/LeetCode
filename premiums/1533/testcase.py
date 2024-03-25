from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[7, 7, 7, 7, 10, 7, 7, 7], Output=4))
		self.testcases.append(case(Input=[6, 6, 12], Output=2))

	def get_testcases(self):
		return self.testcases
