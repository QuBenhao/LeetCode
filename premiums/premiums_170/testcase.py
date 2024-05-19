from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['TwoSum', 'add', 'add', 'add', 'find', 'find'], [[], [1], [3], [5], [4], [7]]], Output=[None, None, None, None, True, False]))

	def get_testcases(self):
		return self.testcases
