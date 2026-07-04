from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['E23', '2X2', '12S'], Output=[7, 1]))
		self.testcases.append(case(Input=['E12', '1X1', '21S'], Output=[4, 2]))
		self.testcases.append(case(Input=['E11', 'XXX', '11S'], Output=[0, 0]))

	def get_testcases(self):
		return self.testcases
