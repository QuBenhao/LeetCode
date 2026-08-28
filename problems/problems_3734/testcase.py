from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['baba', 'abba'], Output="baab"))
		self.testcases.append(case(Input=['baba', 'bbaa'], Output=""))
		self.testcases.append(case(Input=['abc', 'abb'], Output=""))
		self.testcases.append(case(Input=['aac', 'abb'], Output="aca"))

	def get_testcases(self):
		return self.testcases
