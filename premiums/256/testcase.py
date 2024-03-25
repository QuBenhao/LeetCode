from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[17, 2, 17], [16, 16, 5], [14, 3, 19]], Output=10))
		self.testcases.append(case(Input=[[7, 6, 2]], Output=2))

	def get_testcases(self):
		return self.testcases
