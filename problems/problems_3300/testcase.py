from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[10, 12, 13, 14], Output=1))
		self.testcases.append(case(Input=[1, 2, 3, 4], Output=1))
		self.testcases.append(case(Input=[999, 19, 199], Output=10))

	def get_testcases(self):
		return self.testcases
