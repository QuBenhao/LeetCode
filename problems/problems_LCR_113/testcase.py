from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[2, [[1, 0]]], Output=[0, 1]))
		self.testcases.append(case(Input=[4, [[1, 0], [2, 0], [3, 1], [3, 2]]], Output=[0,2,1,3]))
		self.testcases.append(case(Input=[1, []], Output=[0]))

	def get_testcases(self):
		return self.testcases
