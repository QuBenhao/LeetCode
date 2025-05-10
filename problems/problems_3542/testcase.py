from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[0, 2], Output=1))
		self.testcases.append(case(Input=[3, 1, 2, 1], Output=3))
		self.testcases.append(case(Input=[1, 2, 1, 2, 1, 2], Output=4))
		self.testcases.append(case(Input=[3,5,4], Output=3))

	def get_testcases(self):
		return self.testcases
