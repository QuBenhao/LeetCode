from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[1, 6, 9, 5], [5, 2, 3, 10], 8], Output=[1, 7, 14, 19]))
		self.testcases.append(case(Input=[[11, 5, 13], [7, 10, 6], 3], Output=[10, 15, 24]))

	def get_testcases(self):
		return self.testcases
