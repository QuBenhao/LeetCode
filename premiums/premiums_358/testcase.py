from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['aabbcc', 3], Output="abcabc"))
		self.testcases.append(case(Input=['aaabc', 3], Output=""))
		self.testcases.append(case(Input=['aaadbbcc', 2], Output="abacabcd"))

	def get_testcases(self):
		return self.testcases
