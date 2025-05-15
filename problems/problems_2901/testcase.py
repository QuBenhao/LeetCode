from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['bab', 'dab', 'cab'], [1, 2, 2]], Output=['bab', 'cab']))
		self.testcases.append(case(Input=[['a', 'b', 'c', 'd'], [1, 2, 3, 4]], Output=['a', 'b', 'c', 'd']))

	def get_testcases(self):
		return self.testcases
