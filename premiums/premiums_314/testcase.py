from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[3, 9, 20, None, None, 15, 7], Output=[[9], [3, 15], [20], [7]]))
		self.testcases.append(case(Input=[3, 9, 8, 4, 0, 1, 7], Output=[[4], [9], [3, 0, 1], [8], [7]]))
		self.testcases.append(case(Input=[3, 9, 8, 4, 0, 1, 7, None, None, None, 2, 5], Output=[[4], [9, 5], [3, 0, 1], [8, 2], [7]]))

	def get_testcases(self):
		return self.testcases
