from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[1, 2, [[1, 2]]], Output=3))
		self.testcases.append(case(Input=[2, 2, [[3, 5], [2, 4]]], Output=9))
		self.testcases.append(case(Input=[2, 3, [[6, 1, 4], [3, 2, 5]]], Output=16))
		self.testcases.append(case(Input=[1,3,[[1,1,28]]], Output=7))

	def get_testcases(self):
		return self.testcases
