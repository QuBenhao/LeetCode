from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[16, 17, 71, 62, 12, 24, 14], Output=4))
		self.testcases.append(case(Input=[8, 8], Output=2))

	def get_testcases(self):
		return self.testcases
