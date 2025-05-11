from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['10100', '10111', '11111', '10010'], Output=6))
		self.testcases.append(case(Input=[], Output=0))
		self.testcases.append(case(Input=['0'], Output=0))
		self.testcases.append(case(Input=['1'], Output=1))
		self.testcases.append(case(Input=['00'], Output=0))

	def get_testcases(self):
		return self.testcases
