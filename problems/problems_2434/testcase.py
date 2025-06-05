from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="zza", Output="azz"))
		self.testcases.append(case(Input="bac", Output="abc"))
		self.testcases.append(case(Input="bdda", Output="addb"))

	def get_testcases(self):
		return self.testcases
