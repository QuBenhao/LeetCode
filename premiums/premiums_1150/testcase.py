from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[2, 4, 5, 5, 5, 5, 5, 6, 6], 5], Output=True))
		self.testcases.append(case(Input=[[10, 100, 101, 101], 101], Output=False))

	def get_testcases(self):
		return self.testcases
