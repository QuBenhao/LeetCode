from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[3, 1, 4], Output=4))
		self.testcases.append(case(Input=[1, 1, 4], Output=4))
		self.testcases.append(case(Input=[1, 2, 4, 9], Output=6))

	def get_testcases(self):
		return self.testcases
