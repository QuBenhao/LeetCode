from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['abc', 'bcd', 'acef', 'xyz', 'az', 'ba', 'a', 'z'], Output=[['acef'], ['a', 'z'], ['abc', 'bcd', 'xyz'], ['az', 'ba']]))
		self.testcases.append(case(Input=['a'], Output=[['a']]))

	def get_testcases(self):
		return self.testcases
