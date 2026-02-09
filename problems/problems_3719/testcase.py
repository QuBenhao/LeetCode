from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[2, 5, 4, 3], Output=4))
		self.testcases.append(case(Input=[3, 2, 2, 5, 4], Output=5))
		self.testcases.append(case(Input=[1, 2, 3, 2], Output=3))

	def get_testcases(self):
		return self.testcases
