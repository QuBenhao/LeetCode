from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[12, 21, 45, 33, 54], Output=1))
		self.testcases.append(case(Input=[120, 21], Output=1))
		self.testcases.append(case(Input=[21, 120], Output=-1))

	def get_testcases(self):
		return self.testcases
