from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['Fancy', 'append', 'addAll', 'append', 'multAll', 'getIndex', 'addAll', 'append', 'multAll', 'getIndex', 'getIndex', 'getIndex'], [[], [2], [3], [7], [2], [0], [3], [10], [2], [0], [1], [2]]], Output=[None, None, None, None, None, 10, None, None, None, 26, 34, 20]))

	def get_testcases(self):
		return self.testcases
