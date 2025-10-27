from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 0, 2, 0, 3], Output=2))
		self.testcases.append(case(Input=[2, 3, 4, 0, 4, 1, 0], Output=0))
		self.testcases.append(case(Input=[16,13,10,0,0,0,10,6,7,8,7], Output=3))

	def get_testcases(self):
		return self.testcases
