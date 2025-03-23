from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['a', 'b', 'c', 'ab', 'bc', 'abc'], 'abc'], Output=3))
		self.testcases.append(case(Input=[['a', 'a'], 'aa'], Output=2))

	def get_testcases(self):
		return self.testcases
