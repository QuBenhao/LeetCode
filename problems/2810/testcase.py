from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="string", Output="rtsng"))
		self.testcases.append(case(Input="poiinter", Output="ponter"))

	def get_testcases(self):
		return self.testcases
