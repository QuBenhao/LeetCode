from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[3, 6, 7], [2, 4, 7, 9]], Output=2))
		self.testcases.append(case(Input=[[4, 6, 109, 111, 213, 215], [5, 110, 214]], Output=1))

	def get_testcases(self):
		return self.testcases
