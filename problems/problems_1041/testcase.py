from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="GGLLGG", Output=True))
		self.testcases.append(case(Input="GG", Output=False))
		self.testcases.append(case(Input="GL", Output=True))

	def get_testcases(self):
		return self.testcases
