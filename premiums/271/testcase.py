from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['Hello', 'World'], Output=['Hello', 'World']))
		self.testcases.append(case(Input=[''], Output=['']))

	def get_testcases(self):
		return self.testcases
