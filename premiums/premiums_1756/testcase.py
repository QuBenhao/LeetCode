from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['MRUQueue', 'fetch', 'fetch', 'fetch', 'fetch'], [[8], [3], [5], [2], [8]]], Output=[None, 3, 6, 2, 2]))

	def get_testcases(self):
		return self.testcases
