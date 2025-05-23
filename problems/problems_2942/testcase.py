from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['leet', 'code'], 'e'], Output=[0, 1]))
		self.testcases.append(case(Input=[['abc', 'bcd', 'aaaa', 'cbc'], 'a'], Output=[0, 2]))
		self.testcases.append(case(Input=[['abc', 'bcd', 'aaaa', 'cbc'], 'z'], Output=[]))

	def get_testcases(self):
		return self.testcases
