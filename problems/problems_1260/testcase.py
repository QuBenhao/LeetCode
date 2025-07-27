from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1], Output=[[9, 1, 2], [3, 4, 5], [6, 7, 8]]))
		self.testcases.append(case(Input=[[[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]], 4], Output=[[12, 0, 21, 13], [3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10]]))
		self.testcases.append(case(Input=[[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 9], Output=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

	def get_testcases(self):
		return self.testcases
