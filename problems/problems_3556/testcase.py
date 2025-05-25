from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="12234", Output=1469))
		self.testcases.append(case(Input="111", Output=11))

	def get_testcases(self):
		return self.testcases
