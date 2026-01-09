from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['sea', 'eat'], Output=231))
		self.testcases.append(case(Input=['delete', 'leet'], Output=403))

	def get_testcases(self):
		return self.testcases
