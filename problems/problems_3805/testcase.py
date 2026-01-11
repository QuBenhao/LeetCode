from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['fusion', 'layout'], Output=1))
		self.testcases.append(case(Input=['ab', 'aa', 'za', 'aa'], Output=2))

	def get_testcases(self):
		return self.testcases
