from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 2, 3], [5, 6, 7], [9, 10, 11]], Output=11))
		self.testcases.append(case(Input=[[1, 2, 3], [5, 17, 7], [9, 11, 10]], Output=17))

	def get_testcases(self):
		return self.testcases
