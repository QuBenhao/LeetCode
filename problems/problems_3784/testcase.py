from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['aabaac', [1, 2, 3, 4, 1, 10]], Output=11))
		self.testcases.append(case(Input=['abc', [10, 5, 8]], Output=13))
		self.testcases.append(case(Input=['zzzzz', [67, 67, 67, 67, 67]], Output=0))

	def get_testcases(self):
		return self.testcases
