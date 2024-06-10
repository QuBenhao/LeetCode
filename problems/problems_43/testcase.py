from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['2', '3'], Output="6"))
		self.testcases.append(case(Input=['123', '456'], Output="56088"))

	def get_testcases(self):
		return self.testcases
