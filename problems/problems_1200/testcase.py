from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[4, 2, 1, 3], Output=[[1, 2], [2, 3], [3, 4]]))
		self.testcases.append(case(Input=[1, 3, 6, 10, 15], Output=[[1, 3]]))
		self.testcases.append(case(Input=[3, 8, -10, 23, 19, -4, -14, 27], Output=[[-14, -10], [19, 23], [23, 27]]))

	def get_testcases(self):
		return self.testcases
