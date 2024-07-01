from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[0, 32, 10, 43], [[0, 1, 10], [1, 2, 15], [0, 3, 10]], 49], Output=75))
		self.testcases.append(case(Input=[[5, 10, 15, 20], [[0, 1, 10], [1, 2, 10], [0, 3, 10]], 30], Output=25))
		self.testcases.append(case(Input=[[1, 2, 3, 4], [[0, 1, 10], [1, 2, 11], [2, 3, 12], [1, 3, 13]], 50], Output=7))

	def get_testcases(self):
		return self.testcases
