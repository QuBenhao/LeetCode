from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="aaabc", Output=3))
		self.testcases.append(case(Input="cbbd", Output=3))
		self.testcases.append(case(Input="baadccab", Output=4))

	def get_testcases(self):
		return self.testcases
