from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['tars', 'rats', 'arts', 'star'], Output=2))
		self.testcases.append(case(Input=['omv', 'ovm'], Output=1))

	def get_testcases(self):
		return self.testcases
