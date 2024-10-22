from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[12, 12, 30, 24, 24], Output=2))
		self.testcases.append(case(Input=[72, 48, 24, 3], Output=3))

	def get_testcases(self):
		return self.testcases
