from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[9, 3, 15, 20, 7], [9, 15, 7, 20, 3]], Output=[3, 9, 20, None, None, 15, 7]))
		self.testcases.append(case(Input=[[-1], [-1]], Output=[-1]))

	def get_testcases(self):
		return self.testcases
