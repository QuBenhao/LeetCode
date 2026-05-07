from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[2, 1, 3], Output=[2, 2, 3]))
		self.testcases.append(case(Input=[2, 3, 1], Output=[3, 3, 3]))
		self.testcases.append(case(Input=[8,12], Output=[8,12]))
		self.testcases.append(case(Input=[30,21,5,35,24], Output=[35,35,35,35,35]))

	def get_testcases(self):
		return self.testcases
