from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[3, 4], Output=6))
		self.testcases.append(case(Input=[2, 7], Output=15))
		self.testcases.append(case(Input=[6715154,7193485], Output=55012476815))

	def get_testcases(self):
		return self.testcases
