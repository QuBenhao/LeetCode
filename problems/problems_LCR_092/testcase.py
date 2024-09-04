from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="00110", Output=1))
		self.testcases.append(case(Input="010110", Output=2))
		self.testcases.append(case(Input="00011000", Output=2))

	def get_testcases(self):
		return self.testcases
