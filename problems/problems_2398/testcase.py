from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[3, 6, 1, 3, 4], [2, 1, 3, 4, 5], 25], Output=3))
		self.testcases.append(case(Input=[[11, 12, 19], [10, 8, 7], 19], Output=0))
		self.testcases.append(case(Input=[[8,76,74,9,75,71,71,42,15,58,88,38,56,59,10,11],[1,92,41,63,22,37,37,8,68,97,39,59,45,50,29,37],412], Output=3))

	def get_testcases(self):
		return self.testcases
