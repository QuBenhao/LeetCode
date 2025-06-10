from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['12233', 4], Output=-1))
		self.testcases.append(case(Input=['1122211', 3], Output=1))
		self.testcases.append(case(Input=['110', 3], Output=-1))

	def get_testcases(self):
		return self.testcases
