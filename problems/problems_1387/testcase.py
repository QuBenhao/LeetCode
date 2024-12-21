from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[12, 15, 2], Output=13))
		self.testcases.append(case(Input=[7, 11, 4], Output=7))

	def get_testcases(self):
		return self.testcases
