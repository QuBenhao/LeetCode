from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=2736, Output=7236))
		self.testcases.append(case(Input=9973, Output=9973))
		self.testcases.append(case(Input=12, Output=21))
		self.testcases.append(case(Input=98368, Output=98863))

	def get_testcases(self):
		return self.testcases
