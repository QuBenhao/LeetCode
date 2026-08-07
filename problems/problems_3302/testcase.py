from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['vbcca', 'abc'], Output=[0, 1, 2]))
		self.testcases.append(case(Input=['bacdc', 'abc'], Output=[1, 2, 4]))
		self.testcases.append(case(Input=['aaaaaa', 'aaabc'], Output=[]))
		self.testcases.append(case(Input=['abc', 'ab'], Output=[0, 1]))

	def get_testcases(self):
		return self.testcases
