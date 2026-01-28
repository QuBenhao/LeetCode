from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['abcd', 'acbe', ['a', 'b', 'c', 'c', 'e', 'd'], ['b', 'c', 'b', 'e', 'b', 'e'], [2, 5, 5, 1, 2, 20]], Output=28))
		self.testcases.append(case(Input=['aaaa', 'bbbb', ['a', 'c'], ['c', 'b'], [1, 2]], Output=12))
		self.testcases.append(case(Input=['abcd', 'abce', ['a'], ['e'], [10000]], Output=-1))

	def get_testcases(self):
		return self.testcases
