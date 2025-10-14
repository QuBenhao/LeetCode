from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[2, 5, 7, 8, 9, 2, 3, 4, 3, 1], 3], Output=True))
		self.testcases.append(case(Input=[[1, 2, 3, 4, 4, 4, 4, 5, 6, 7], 5], Output=False))
		self.testcases.append(case(Input=[[-15,3,16,0],2], Output=False))
		self.testcases.append(case(Input=[[-15,19],1], Output=True))
		self.testcases.append(case(Input=[[19,4,19,6,18],2], Output=True))

	def get_testcases(self):
		return self.testcases
