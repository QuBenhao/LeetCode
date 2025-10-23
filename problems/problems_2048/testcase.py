from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=1, Output=22))
		self.testcases.append(case(Input=1000, Output=1333))
		self.testcases.append(case(Input=3000, Output=3133))

	def get_testcases(self):
		return self.testcases
