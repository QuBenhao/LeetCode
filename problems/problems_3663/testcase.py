from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=1553322, Output=1))
		self.testcases.append(case(Input=723344511, Output=2))

	def get_testcases(self):
		return self.testcases
