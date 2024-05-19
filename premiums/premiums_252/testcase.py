from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[0, 30], [5, 10], [15, 20]], Output=False))
		self.testcases.append(case(Input=[[7, 10], [2, 4]], Output=True))

	def get_testcases(self):
		return self.testcases
