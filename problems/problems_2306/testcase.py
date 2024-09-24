from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['coffee', 'donuts', 'time', 'toffee'], Output=6))
		self.testcases.append(case(Input=['lack', 'back'], Output=0))

	def get_testcases(self):
		return self.testcases
