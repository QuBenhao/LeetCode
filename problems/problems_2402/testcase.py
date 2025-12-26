from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[2, [[0, 10], [1, 5], [2, 7], [3, 4]]], Output=0))
		self.testcases.append(case(Input=[3, [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]], Output=1))

	def get_testcases(self):
		return self.testcases
