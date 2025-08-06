from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 2, 3, 4], [5, 6, 8, 7], [9, 10, 11, 12], [13, 14, 15, 16]], Output=100))
		self.testcases.append(case(Input=[[1, 1], [1, 1]], Output=4))
		self.testcases.append(case(Input=[[4,18,19,9,20,14],[16,4,4,16,15,16],[2,11,15,6,8,9],[6,7,11,17,7,6],[17,17,2,13,2,14],[16,9,6,14,7,16]], Output=182))

	def get_testcases(self):
		return self.testcases
