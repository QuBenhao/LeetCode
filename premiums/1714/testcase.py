from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[0, 1, 2, 3, 4, 5, 6, 7], [[0, 3], [5, 1], [4, 2]]], Output=[9, 18, 10]))
		self.testcases.append(case(Input=[[100, 200, 101, 201, 102, 202, 103, 203], [[0, 7]]], Output=[303]))

	def get_testcases(self):
		return self.testcases
