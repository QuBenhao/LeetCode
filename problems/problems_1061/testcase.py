from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['parker', 'morris', 'parser'], Output="makkek"))
		self.testcases.append(case(Input=['hello', 'world', 'hold'], Output="hdld"))
		self.testcases.append(case(Input=['leetcode', 'programs', 'sourcecode'], Output="aauaaaaada"))

	def get_testcases(self):
		return self.testcases
