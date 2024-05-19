from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['anagram', 'nagaram'], Output=True))
		self.testcases.append(case(Input=['rat', 'car'], Output=False))

	def get_testcases(self):
		return self.testcases
