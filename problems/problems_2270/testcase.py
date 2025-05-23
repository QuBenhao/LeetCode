from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[10, 4, -8, 7], Output=2))
		self.testcases.append(case(Input=[2, 3, 1, 0], Output=2))
		self.testcases.append(case(Input=[0,0], Output=1))

	def get_testcases(self):
		return self.testcases
