from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[3, 6, 5, 1, 8], Output=18))
		self.testcases.append(case(Input=[4], Output=0))
		self.testcases.append(case(Input=[1, 2, 3, 4, 4], Output=12))

	def get_testcases(self):
		return self.testcases
