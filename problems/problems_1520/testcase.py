from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="adefaddaccc", Output=['e', 'f', 'ccc']))
		self.testcases.append(case(Input="abbaccd", Output=['d', 'bb', 'cc']))

	def get_testcases(self):
		return self.testcases
