from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['bcca', 'abc'], Output=1))
		self.testcases.append(case(Input=['abcabc', 'abc'], Output=10))
		self.testcases.append(case(Input=['abcabc', 'aaabc'], Output=0))

	def get_testcases(self):
		return self.testcases
