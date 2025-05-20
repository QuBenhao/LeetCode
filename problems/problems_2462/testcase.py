from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[17, 12, 10, 2, 7, 2, 11, 20, 8], 3, 4], Output=11))
		self.testcases.append(case(Input=[[1, 2, 4, 1], 3, 3], Output=4))
		self.testcases.append(case(Input=[[31,25,72,79,74,65,84,91,18,59,27,9,81,33,17,58],11,2], Output=423))

	def get_testcases(self):
		return self.testcases
