from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[2, 1], [5, 0], [4, 2]], Output=10))
		self.testcases.append(case(Input=[[3, 0], [0, 3]], Output=3))
		self.testcases.append(case(Input=[[6,10],[10,4],[8,2],[5,2],[9,4],[6,6],[5,5],[7,3]], Output=30))

	def get_testcases(self):
		return self.testcases
