from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['abc', 4], Output=3))
		self.testcases.append(case(Input=['abcde', 5], Output=5))
		self.testcases.append(case(Input=['abcdABCD1234', 12], Output=12))

	def get_testcases(self):
		return self.testcases
