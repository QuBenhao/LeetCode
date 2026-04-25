from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['a', 'a', 'a', 'a'], ['a', 'b', 'b', 'a'], ['a', 'b', 'b', 'a'], ['a', 'a', 'a', 'a']], Output=True))
		self.testcases.append(case(Input=[['c', 'c', 'c', 'a'], ['c', 'd', 'c', 'c'], ['c', 'c', 'e', 'c'], ['f', 'c', 'c', 'c']], Output=True))
		self.testcases.append(case(Input=[['a', 'b', 'b'], ['b', 'z', 'b'], ['b', 'b', 'a']], Output=False))

	def get_testcases(self):
		return self.testcases
