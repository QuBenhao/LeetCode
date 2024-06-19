from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['abcd', 'bnrt', 'crmy', 'dtye'], Output=True))
		self.testcases.append(case(Input=['abcd', 'bnrt', 'crm', 'dt'], Output=True))
		self.testcases.append(case(Input=['ball', 'area', 'read', 'lady'], Output=False))

	def get_testcases(self):
		return self.testcases
