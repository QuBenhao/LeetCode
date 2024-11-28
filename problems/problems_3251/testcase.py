from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[2, 3, 2], Output=4))
		self.testcases.append(case(Input=[5, 5, 5, 5], Output=126))

	def get_testcases(self):
		return self.testcases
