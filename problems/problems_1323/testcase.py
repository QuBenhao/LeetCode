from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=9669, Output=9969))
		self.testcases.append(case(Input=9996, Output=9999))
		self.testcases.append(case(Input=9999, Output=9999))

	def get_testcases(self):
		return self.testcases
