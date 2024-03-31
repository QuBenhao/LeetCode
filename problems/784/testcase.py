from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="a1b2", Output=['a1b2', 'a1B2', 'A1b2', 'A1B2']))
		self.testcases.append(case(Input="3z4", Output=['3z4', '3Z4']))

	def get_testcases(self):
		return self.testcases
