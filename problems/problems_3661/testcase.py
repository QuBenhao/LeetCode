from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[4], [3], [1, 10]], Output=1))
		self.testcases.append(case(Input=[[10, 2], [5, 1], [5, 2, 7]], Output=3))
		self.testcases.append(case(Input=[[1, 2], [100, 1], [10]], Output=0))
		self.testcases.append(case(Input=[[17,59,32,11,72,18],[5,7,6,5,2,10],[17,25,33,29,54,53,18,35,39,37,20,14,34,13,16,58,22,51,56,27,10,15,12,23,45,43,21,2,42,7,32,40,8,9,1,5,55,30,38,4,3,31,36,41,57,28,11,49,26,19,50,52,6,47,46,44,24,48]], Output=37))

	def get_testcases(self):
		return self.testcases
