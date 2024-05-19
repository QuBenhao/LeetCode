from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[3, 2, 2, [1, 1], [2, 2]], Output=2))
		self.testcases.append(case(Input=[3, 4, 3, [1, 2], [2, 3]], Output=9))

	def get_testcases(self):
		return self.testcases
