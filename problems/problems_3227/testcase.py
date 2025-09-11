from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="leetcoder", Output=True))
		self.testcases.append(case(Input="bbcd", Output=False))

	def get_testcases(self):
		return self.testcases
