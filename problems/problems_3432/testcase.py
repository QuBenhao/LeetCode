from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[10, 10, 3, 7, 6], Output=4))
		self.testcases.append(case(Input=[1, 2, 2], Output=0))
		self.testcases.append(case(Input=[2, 4, 6, 8], Output=3))

	def get_testcases(self):
		return self.testcases
