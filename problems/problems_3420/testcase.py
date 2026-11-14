from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[6, 3, 1, 2, 4, 4], 7], Output=17))
		self.testcases.append(case(Input=[[6, 3, 1, 3, 6], 4], Output=12))

	def get_testcases(self):
		return self.testcases
