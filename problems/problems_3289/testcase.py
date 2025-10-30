from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[0, 1, 1, 0], Output=[0, 1]))
		self.testcases.append(case(Input=[0, 3, 2, 1, 3, 2], Output=[2, 3]))
		self.testcases.append(case(Input=[7, 1, 5, 4, 3, 4, 6, 0, 9, 5, 8, 2], Output=[4, 5]))
		self.testcases.append(case(Input=[2,0,1,2,1], Output=[1,2]))

	def get_testcases(self):
		return self.testcases
