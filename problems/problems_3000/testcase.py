from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[9, 3], [8, 6]], Output=48))
		self.testcases.append(case(Input=[[3, 4], [4, 3]], Output=12))

	def get_testcases(self):
		return self.testcases
