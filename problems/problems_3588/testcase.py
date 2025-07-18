from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 1], [1, 2], [3, 2], [3, 3]], Output=2))
		self.testcases.append(case(Input=[[1, 1], [2, 2], [3, 3]], Output=-1))
		self.testcases.append(case(Input=[[1,1],[7,7],[3,2],[3,16]], Output=56))

	def get_testcases(self):
		return self.testcases
