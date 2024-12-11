from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[8, 5, 2], [6, 4, 1], [9, 7, 3]], Output=285))
		self.testcases.append(case(Input=[[10, 8, 6, 4, 2], [9, 7, 5, 3, 2]], Output=386))

	def get_testcases(self):
		return self.testcases
