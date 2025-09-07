from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[2, 5, 3, 1, 4], Output=2))
		self.testcases.append(case(Input=[5, 1, 2, 3, 4], Output=3))
		self.testcases.append(case(Input=[1000000000, 999999999, 999999998], Output=0))
		self.testcases.append(case(Input=[2,5,3,1,4], Output=2))

	def get_testcases(self):
		return self.testcases
