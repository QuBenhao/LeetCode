from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['apple', ['blade']], Output="a4"))
		self.testcases.append(case(Input=['apple', ['blade', 'plain', 'amber']], Output="1p3"))

	def get_testcases(self):
		return self.testcases
