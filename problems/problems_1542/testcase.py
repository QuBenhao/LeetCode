from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="3242415", Output=5))
		self.testcases.append(case(Input="12345678", Output=1))
		self.testcases.append(case(Input="213123", Output=6))

	def get_testcases(self):
		return self.testcases
