from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="hello", Output=13))
		self.testcases.append(case(Input="zaz", Output=50))

	def get_testcases(self):
		return self.testcases
