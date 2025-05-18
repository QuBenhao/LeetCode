from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[37, 100], Output=1))
		self.testcases.append(case(Input=[22, 14, 33, 7], Output=0))
		self.testcases.append(case(Input=[18, 43, 34, 16], Output=2))

	def get_testcases(self):
		return self.testcases
