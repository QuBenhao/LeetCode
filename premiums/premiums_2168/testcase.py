from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="5", Output=5))
		self.testcases.append(case(Input="9", Output=9))

	def get_testcases(self):
		return self.testcases
