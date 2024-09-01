from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['TTFF', 2], Output=4))
		self.testcases.append(case(Input=['TFFT', 1], Output=3))
		self.testcases.append(case(Input=['TTFTTFTT', 1], Output=5))

	def get_testcases(self):
		return self.testcases
