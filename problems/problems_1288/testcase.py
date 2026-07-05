from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 4], [3, 6], [2, 8]], Output=2))
		self.testcases.append(case(Input=[[1, 4], [2, 3]], Output=1))

	def get_testcases(self):
		return self.testcases
