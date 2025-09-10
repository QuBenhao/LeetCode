from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="lEetcOde", Output="lEOtcede"))
		self.testcases.append(case(Input="lYmpH", Output="lYmpH"))

	def get_testcases(self):
		return self.testcases
