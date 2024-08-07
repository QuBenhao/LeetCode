from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['cbaebabacd', 'abc'], Output=[0, 6]))
		self.testcases.append(case(Input=['abab', 'ab'], Output=[0, 1, 2]))

	def get_testcases(self):
		return self.testcases
