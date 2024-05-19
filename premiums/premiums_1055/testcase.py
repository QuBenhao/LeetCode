from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['abc', 'abcbc'], Output=2))
		self.testcases.append(case(Input=['abc', 'acdbc'], Output=-1))
		self.testcases.append(case(Input=['xyz', 'xzyxz'], Output=3))

	def get_testcases(self):
		return self.testcases
