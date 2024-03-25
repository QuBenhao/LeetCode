from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[12, 6, 3, 14, 8], Output=2))
		self.testcases.append(case(Input=[4, 12, 6, 14], Output=1))

	def get_testcases(self):
		return self.testcases
