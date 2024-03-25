from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=4, Output="((1,4),(2,3))"))
		self.testcases.append(case(Input=8, Output="(((1,8),(4,5)),((2,7),(3,6)))"))

	def get_testcases(self):
		return self.testcases
