from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 2, 3, 4], Output=[-1, -1, -1, -1]))
		self.testcases.append(case(Input=[1, 2, 0, 0, 2, 1], Output=[-1, -1, 2, 1, -1, -1]))
		self.testcases.append(case(Input=[1, 2, 0, 1, 2], Output=[]))
		self.testcases.append(case(Input=[69,0,0,0,69], Output=[-1,69,1,1,-1]))

	def get_testcases(self):
		return self.testcases
