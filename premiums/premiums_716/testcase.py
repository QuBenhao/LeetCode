from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['MaxStack', 'push', 'push', 'push', 'top', 'popMax', 'top', 'peekMax', 'pop', 'top'], [[], [5], [1], [5], [], [], [], [], [], []]], Output=[None, None, None, None, 5, 5, 1, 5, 1, 5]))

	def get_testcases(self):
		return self.testcases
