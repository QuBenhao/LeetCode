from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 2, 3, 4, 5, 6, 7], Output=12))
		self.testcases.append(case(Input=[5, 6, 4], Output=0))
		self.testcases.append(case(Input=[64, 8, 32], Output=2048))

	def get_testcases(self):
		return self.testcases
