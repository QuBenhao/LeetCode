from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['abcd', 'acbd', 'aacd'], Output=True))
		self.testcases.append(case(Input=['ab', 'cd', 'yz'], Output=False))
		self.testcases.append(case(Input=['abcd', 'cccc', 'abyd', 'abab'], Output=True))

	def get_testcases(self):
		return self.testcases
