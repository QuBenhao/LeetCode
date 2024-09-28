from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['Solution', 'pickIndex'], [[[1]], []]], Output=[None, 0]))
		self.testcases.append(case(Input=[['Solution', 'pickIndex', 'pickIndex', 'pickIndex', 'pickIndex', 'pickIndex'], [[[1, 3]], [], [], [], [], []]], Output=[None, 1, 1, 1, 1, 0]))

	def get_testcases(self):
		return self.testcases
