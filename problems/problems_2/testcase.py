from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[2, 4, 3], [5, 6, 4]], Output=[7, 0, 8]))
		self.testcases.append(case(Input=[[0], [0]], Output=[0]))
		self.testcases.append(case(Input=[[9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]], Output=[8, 9, 9, 9, 0, 0, 0, 1]))

	def get_testcases(self):
		return self.testcases
