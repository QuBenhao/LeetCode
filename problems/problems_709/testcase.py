from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="Hello", Output="hello"))
		self.testcases.append(case(Input="here", Output="here"))
		self.testcases.append(case(Input="LOVELY", Output="lovely"))

	def get_testcases(self):
		return self.testcases
