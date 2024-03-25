from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[0, 0], [0, 5], [5, 5], [5, 0]], Output=True))
		self.testcases.append(case(Input=[[0, 0], [0, 10], [10, 10], [10, 0], [5, 5]], Output=False))

	def get_testcases(self):
		return self.testcases
