from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]], Output=120))
		self.testcases.append(case(Input=[[1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60]], Output=150))
		self.testcases.append(case(Input=[[1, 1, 1], [2, 3, 4], [5, 6, 4]], Output=6))

	def get_testcases(self):
		return self.testcases
