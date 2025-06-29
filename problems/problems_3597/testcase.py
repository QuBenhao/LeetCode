from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="abbccccd", Output=['a', 'b', 'bc', 'c', 'cc', 'd']))
		self.testcases.append(case(Input="aaaa", Output=['a', 'aa']))

	def get_testcases(self):
		return self.testcases
