from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 0], [2, 3], [5, 4, 3], [8, 2, 6, 7]], Output=18))
		self.testcases.append(case(Input=[[0, 0], [0, 0], [5], [26]], Output=0))

	def get_testcases(self):
		return self.testcases
