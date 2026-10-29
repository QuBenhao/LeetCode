from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[3, [[0, 1, 1], [1, 2, 1], [0, 2, 3]], 'aab', 1], Output=3))
		self.testcases.append(case(Input=[3, [[0, 1, 1], [1, 2, 1], [0, 2, 3]], 'aab', 2], Output=2))
		self.testcases.append(case(Input=[3, [[0, 1, 1], [1, 2, 1]], 'aaa', 2], Output=-1))

	def get_testcases(self):
		return self.testcases
