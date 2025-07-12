from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="  this   is  a sentence ", Output="this   is   a   sentence"))
		self.testcases.append(case(Input=" practice   makes   perfect", Output="practice   makes   perfect "))

	def get_testcases(self):
		return self.testcases
