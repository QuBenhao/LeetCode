from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="abbcccc", Output=5))
		self.testcases.append(case(Input="abcd", Output=1))
		self.testcases.append(case(Input="aaaa", Output=4))

	def get_testcases(self):
		return self.testcases
