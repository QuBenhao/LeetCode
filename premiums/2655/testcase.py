from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[10, [[3, 5], [7, 8]]], Output=[[0, 2], [6, 6], [9, 9]]))
		self.testcases.append(case(Input=[3, [[0, 2]]], Output=[]))
		self.testcases.append(case(Input=[7, [[2, 4], [0, 3]]], Output=[[5, 6]]))

	def get_testcases(self):
		return self.testcases
