from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[[0, 2], [3, 4], [5, 7]], [1, 6]], Output=[[0, 1], [6, 7]]))
		self.testcases.append(case(Input=[[[0, 5]], [2, 3]], Output=[[0, 2], [3, 5]]))
		self.testcases.append(case(Input=[[[-5, -4], [-3, -2], [1, 2], [3, 5], [8, 9]], [-1, 4]], Output=[[-5, -4], [-3, -2], [4, 5], [8, 9]]))

	def get_testcases(self):
		return self.testcases
