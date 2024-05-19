from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="#11ee66", Output="#11ee66"))
		self.testcases.append(case(Input="#5544dd", Output="#5544dd"))

	def get_testcases(self):
		return self.testcases
