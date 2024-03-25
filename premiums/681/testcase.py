from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="19:39", Output="19:39"))
		self.testcases.append(case(Input="22:22", Output="22:22"))

	def get_testcases(self):
		return self.testcases
