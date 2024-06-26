from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['MyHashMap', 'put', 'put', 'get', 'get', 'put', 'get', 'remove', 'get'], [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]], Output=[None, None, None, 1, -1, None, 1, None, -1]))

	def get_testcases(self):
		return self.testcases
