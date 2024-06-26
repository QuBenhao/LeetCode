from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="ababcbacadefegdehijhklij", Output=[9, 7, 8]))
		self.testcases.append(case(Input="eccbbbbdec", Output=[10]))

	def get_testcases(self):
		return self.testcases
