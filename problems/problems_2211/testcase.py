from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="RLRSLL", Output=5))
		self.testcases.append(case(Input="LLRR", Output=0))
		self.testcases.append(case(Input="LSSSLLSSSSLRRSLLLSLSLRRLLLLLRSSRSRRSLLLSSS", Output=24))

	def get_testcases(self):
		return self.testcases
