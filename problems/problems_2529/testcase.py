from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[-2, -1, -1, 1, 2, 3], Output=3))
		self.testcases.append(case(Input=[-3, -2, -1, 0, 0, 1, 2], Output=3))
		self.testcases.append(case(Input=[5, 20, 66, 1314], Output=4))

	def get_testcases(self):
		return self.testcases
