from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[[1, 0, 0], [-1, 0, 3]], [[7, 0, 0], [0, 0, 0], [0, 0, 1]]], Output=[[7, 0, 0], [-7, 0, 3]]))
		self.testcases.append(case(Input=[[[0]], [[0]]], Output=[[0]]))

	def get_testcases(self):
		return self.testcases
