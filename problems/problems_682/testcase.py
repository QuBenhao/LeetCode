from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['5', '2', 'C', 'D', '+'], Output=30))
		self.testcases.append(case(Input=['5', '-2', '4', 'C', 'D', '9', '+', '+'], Output=27))
		self.testcases.append(case(Input=['1', 'C'], Output=0))

	def get_testcases(self):
		return self.testcases
