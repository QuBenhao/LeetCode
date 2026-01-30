from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['c', 'f', 'j'], 'a'], Output="c"))
		self.testcases.append(case(Input=[['c', 'f', 'j'], 'c'], Output="f"))
		self.testcases.append(case(Input=[['x', 'x', 'y', 'y'], 'z'], Output="x"))

	def get_testcases(self):
		return self.testcases
