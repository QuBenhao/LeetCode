from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['horse', 'ros'], Output=3))
		self.testcases.append(case(Input=['intention', 'execution'], Output=5))

	def get_testcases(self):
		return self.testcases
