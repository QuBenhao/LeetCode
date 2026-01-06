from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 2, 3, 4, 5, 6], Output=110))
		self.testcases.append(case(Input=[1, None, 2, 3, 4, None, None, 5, 6], Output=90))

	def get_testcases(self):
		return self.testcases
