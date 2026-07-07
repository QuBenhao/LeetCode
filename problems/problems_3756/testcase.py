from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['10203004', [[0, 7], [1, 3], [4, 6]]], Output=[12340, 4, 9]))
		self.testcases.append(case(Input=['1000', [[0, 3], [1, 1]]], Output=[1, 0]))
		self.testcases.append(case(Input=['9876543210', [[0, 9]]], Output=[444444137]))

	def get_testcases(self):
		return self.testcases
