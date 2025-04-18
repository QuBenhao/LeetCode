from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['time', 'me', 'bell'], Output=10))
		self.testcases.append(case(Input=['t'], Output=2))

	def get_testcases(self):
		return self.testcases
