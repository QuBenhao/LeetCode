from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 1], Output=0))
		self.testcases.append(case(Input=[2, 1], Output=0))
		self.testcases.append(case(Input=[2, 2], Output=1))
		self.testcases.append(case(Input=[3,1], Output=0))

	def get_testcases(self):
		return self.testcases
