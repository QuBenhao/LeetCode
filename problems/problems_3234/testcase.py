from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="00011", Output=5))
		self.testcases.append(case(Input="101101", Output=16))

	def get_testcases(self):
		return self.testcases
