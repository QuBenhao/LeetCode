from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['alex', 'loves', 'leetcode'], Output="alexlovesleetcode"))
		self.testcases.append(case(Input=['catg', 'ctaagt', 'gcta', 'ttca', 'atgcatc'], Output="gctaagttcatgcatc"))

	def get_testcases(self):
		return self.testcases
