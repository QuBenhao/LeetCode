from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['abcw', 'baz', 'foo', 'bar', 'xtfn', 'abcdef'], Output=16))
		self.testcases.append(case(Input=['a', 'ab', 'abc', 'd', 'cd', 'bcd', 'abcd'], Output=4))
		self.testcases.append(case(Input=['a', 'aa', 'aaa', 'aaaa'], Output=0))

	def get_testcases(self):
		return self.testcases
