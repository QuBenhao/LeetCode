from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['abba', 2], Output="baab"))
		self.testcases.append(case(Input=['aa', 2], Output=""))
		self.testcases.append(case(Input=['bacab', 1], Output="abcba"))

	def get_testcases(self):
		return self.testcases
