from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=7, Output=[[0, 0, 0, None, None, 0, 0, None, None, 0, 0], [0, 0, 0, None, None, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, None, None, None, None, 0, 0], [0, 0, 0, 0, 0, None, None, 0, 0]]))
		self.testcases.append(case(Input=3, Output=[[0, 0, 0]]))

	def get_testcases(self):
		return self.testcases
