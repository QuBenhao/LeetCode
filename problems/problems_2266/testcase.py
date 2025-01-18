from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="22233", Output=8))
		self.testcases.append(case(Input="222222222222222222222222222222222222", Output=82876089))

	def get_testcases(self):
		return self.testcases
