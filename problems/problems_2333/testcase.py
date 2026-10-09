from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 2, 3, 4], [2, 10, 20, 19], 0, 0], Output=579))
		self.testcases.append(case(Input=[[1, 4, 10, 12], [5, 8, 6, 9], 1, 1], Output=43))

	def get_testcases(self):
		return self.testcases
