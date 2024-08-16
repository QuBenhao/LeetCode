from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['leetcodeleet', 4], Output=1))
		self.testcases.append(case(Input=['leetcoleet', 2], Output=3))

	def get_testcases(self):
		return self.testcases
