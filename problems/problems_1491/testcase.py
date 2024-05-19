from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[4000, 3000, 1000, 2000], Output=2500.0))
		self.testcases.append(case(Input=[1000, 2000, 3000], Output=2000.0))

	def get_testcases(self):
		return self.testcases
