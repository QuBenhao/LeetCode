from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[2, [1, 2], [4, 3], [[1, 2]], 3], Output=5))
		self.testcases.append(case(Input=[2, [3, 4], [5, 8], [[1, 2]], 4], Output=4))
		self.testcases.append(case(Input=[3, [4, 6, 8], [7, 9, 11], [[1, 2], [1, 3]], 10], Output=10))
		self.testcases.append(case(Input=[3, [5, 2, 3], [8, 5, 6], [[1, 2], [2, 3]], 7], Output=12))

	def get_testcases(self):
		return self.testcases
