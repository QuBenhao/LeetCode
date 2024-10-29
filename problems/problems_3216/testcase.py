from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="45320", Output="43520"))
		self.testcases.append(case(Input="001", Output="001"))

	def get_testcases(self):
		return self.testcases
