from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['zbbz', 3], Output="aaaz"))
		self.testcases.append(case(Input=['xaxcd', 4], Output="aawcd"))
		self.testcases.append(case(Input=['lol', 0], Output="lol"))

	def get_testcases(self):
		return self.testcases
