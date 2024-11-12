from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['0001111', 2, [[0, 6]]], Output=[26]))
		self.testcases.append(case(Input=['010101', 1, [[0, 5], [1, 4], [2, 3]]], Output=[15, 9, 3]))

	def get_testcases(self):
		return self.testcases
