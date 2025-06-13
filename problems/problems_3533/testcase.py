from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[3, 12, 45], 5], Output=[3, 12, 45]))
		self.testcases.append(case(Input=[[10, 5], 10], Output=[5, 10]))
		self.testcases.append(case(Input=[[1, 2, 3], 5], Output=[]))
		self.testcases.append(case(Input=[[25900,39695,2584,18305,75986,79563,56939,36282,89720,16517,28547,24732],57], Output=[]))

	def get_testcases(self):
		return self.testcases
