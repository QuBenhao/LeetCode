from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[3, 2, 4, 5, 0], Output=4))
		self.testcases.append(case(Input=[2, 2, 3, 4], Output=0))
		self.testcases.append(case(Input=[0], Output=0))

	def get_testcases(self):
		return self.testcases
