from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 1, 0, 0], Output=[[0]]))
		self.testcases.append(case(Input=[3, 4, 0, 0], Output=[[0, 3, 6, 9], [11, 8, 1, 4], [2, 5, 10, 7]]))

	def get_testcases(self):
		return self.testcases
