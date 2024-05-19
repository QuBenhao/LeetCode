from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[5, 7, [2, 2], [4, 4], [[3, 0], [2, 5]]], Output=12))
		self.testcases.append(case(Input=[1, 3, [0, 1], [0, 0], [[0, 2]]], Output=3))

	def get_testcases(self):
		return self.testcases
