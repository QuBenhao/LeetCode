from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[3, 7], Output=[[1, 2, 4]]))
		self.testcases.append(case(Input=[3, 9], Output=[[1, 2, 6], [1, 3, 5], [2, 3, 4]]))
		self.testcases.append(case(Input=[4, 1], Output=[]))

	def get_testcases(self):
		return self.testcases
