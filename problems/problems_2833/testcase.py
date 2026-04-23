from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="L_RL__R", Output=3))
		self.testcases.append(case(Input="_R__LL_", Output=5))
		self.testcases.append(case(Input="_______", Output=7))

	def get_testcases(self):
		return self.testcases
