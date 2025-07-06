from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[2, [[0, 1, 3]], 2], Output=3))
		self.testcases.append(case(Input=[3, [[0, 1, 2], [1, 2, 4]], 3], Output=4))
		self.testcases.append(case(Input=[3, [[0, 2, 5]], 2], Output=0))

	def get_testcases(self):
		return self.testcases
