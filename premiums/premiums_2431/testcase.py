from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[10, 20, 20], [5, 8, 8], 20, 1], Output=13))
		self.testcases.append(case(Input=[[10, 15, 7], [5, 8, 20], 10, 2], Output=28))

	def get_testcases(self):
		return self.testcases
