from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[10, 20], [2, 17, 18, 19], 2], Output=16))
		self.testcases.append(case(Input=[[20, 30, 10], [19, 13, 26, 4, 25, 11, 21], 2], Output=20))
		self.testcases.append(case(Input=[[3],[2,4],2], Output=3))
		self.testcases.append(case(Input=[[2],[2],2], Output=1))
		self.testcases.append(case(Input=[[8,7],[7,3,8,5,2],3], Output=6))

	def get_testcases(self):
		return self.testcases
