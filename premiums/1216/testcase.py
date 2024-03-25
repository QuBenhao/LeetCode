from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['abcdeca', 2], Output=True))
		self.testcases.append(case(Input=['abbababa', 1], Output=True))

	def get_testcases(self):
		return self.testcases
