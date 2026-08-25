from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['100011001', 3], Output="11001"))
		self.testcases.append(case(Input=['1011', 2], Output="11"))
		self.testcases.append(case(Input=['000', 1], Output=""))

	def get_testcases(self):
		return self.testcases
