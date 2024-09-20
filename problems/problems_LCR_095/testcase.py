from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['abcde', 'ace'], Output=3))
		self.testcases.append(case(Input=['abc', 'abc'], Output=3))
		self.testcases.append(case(Input=['abc', 'def'], Output=0))

	def get_testcases(self):
		return self.testcases
