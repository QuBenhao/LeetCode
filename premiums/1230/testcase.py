from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[0.4], 1], Output=0.4))
		self.testcases.append(case(Input=[[0.5, 0.5, 0.5, 0.5, 0.5], 0], Output=0.03125))

	def get_testcases(self):
		return self.testcases
