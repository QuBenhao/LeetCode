from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 2], [3, 4]], Output=6))
		self.testcases.append(case(Input=[[6, 7], [5, 8]], Output=9))
		self.testcases.append(case(Input=[[2, 7, 5]], Output=0))

	def get_testcases(self):
		return self.testcases
