from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[12, 9], 1], Output=30))
		self.testcases.append(case(Input=[[8, 1, 2], 2], Output=35))

	def get_testcases(self):
		return self.testcases
