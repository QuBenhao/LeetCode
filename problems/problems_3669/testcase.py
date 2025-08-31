from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[100, 2], Output=[10, 10]))
		self.testcases.append(case(Input=[44, 3], Output=[2, 2, 11]))
		self.testcases.append(case(Input=[65536,5], Output=[8,8,8,8,16]))

	def get_testcases(self):
		return self.testcases
