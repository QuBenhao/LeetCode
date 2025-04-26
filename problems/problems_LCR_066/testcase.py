from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['MapSum', 'insert', 'sum', 'insert', 'sum'], [[], ['apple', 3], ['ap'], ['app', 2], ['ap']]], Output=[None, None, 3, None, 5]))

	def get_testcases(self):
		return self.testcases
