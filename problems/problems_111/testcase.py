from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[3, 9, 20, None, None, 15, 7], Output=2))
		self.testcases.append(case(Input=[2, None, 3, None, 4, None, 5, None, 6], Output=5))

	def get_testcases(self):
		return self.testcases
