from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['c'], [0]], Output=['e', 'b']))
		self.testcases.append(case(Input=[['d'], [1]], Output=['a', 'b', 'c']))

	def get_testcases(self):
		return self.testcases
