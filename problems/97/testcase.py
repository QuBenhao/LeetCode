from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['aabcc', 'dbbca', 'aadbbcbcac'], Output=True))
		self.testcases.append(case(Input=['aabcc', 'dbbca', 'aadbbbaccc'], Output=False))
		self.testcases.append(case(Input=['', '', ''], Output=True))

	def get_testcases(self):
		return self.testcases
