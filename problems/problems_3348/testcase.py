from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['1234', 256], Output="1488"))
		self.testcases.append(case(Input=['12355', 50], Output="12355"))
		self.testcases.append(case(Input=['11111', 26], Output="-1"))

	def get_testcases(self):
		return self.testcases
