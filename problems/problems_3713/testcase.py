from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="abbac", Output=4))
		self.testcases.append(case(Input="zzabccy", Output=4))
		self.testcases.append(case(Input="aba", Output=2))

	def get_testcases(self):
		return self.testcases
