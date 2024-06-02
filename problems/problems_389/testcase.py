from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['abcd', 'abcde'], Output="e"))
		self.testcases.append(case(Input=['', 'y'], Output="y"))

	def get_testcases(self):
		return self.testcases
