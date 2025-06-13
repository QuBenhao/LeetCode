from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['011001', '000000', '010100', '001000'], Output=8))
		self.testcases.append(case(Input=['000', '111', '000'], Output=0))

	def get_testcases(self):
		return self.testcases
