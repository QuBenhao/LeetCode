from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[10, 20], [2, 17, 18, 19], 2], Output=16))
		self.testcases.append(case(Input=[[20, 30, 10], [19, 13, 26, 4, 25, 11, 21], 2], Output=20))

	def get_testcases(self):
		return self.testcases
