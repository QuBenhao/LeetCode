from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['abcd', 'bcd', 'xbcd'], ['cd', 'bcd', 'xyz']], Output=[1, 1, 1]))
		self.testcases.append(case(Input=[['abcdefgh', 'poiuygh', 'ghghgh'], ['gh', 'acbfgh', 'acbfegh']], Output=[2, 0, 2]))

	def get_testcases(self):
		return self.testcases
