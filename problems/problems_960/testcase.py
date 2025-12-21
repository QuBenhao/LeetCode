from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['babca', 'bbazb'], Output=3))
		self.testcases.append(case(Input=['edcba'], Output=4))
		self.testcases.append(case(Input=['ghi', 'def', 'abc'], Output=0))

	def get_testcases(self):
		return self.testcases
