from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[2, 7], Output="Alice"))
		self.testcases.append(case(Input=[4, 11], Output="Bob"))

	def get_testcases(self):
		return self.testcases
