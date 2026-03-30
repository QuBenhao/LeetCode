from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['TFTF', 'ab'], Output="ababa"))
		self.testcases.append(case(Input=['TFTF', 'abc'], Output=""))
		self.testcases.append(case(Input=['F', 'd'], Output="a"))

	def get_testcases(self):
		return self.testcases
