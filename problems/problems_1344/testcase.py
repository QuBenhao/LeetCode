from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[12, 30], Output=165))
		self.testcases.append(case(Input=[3, 30], Output=75))
		self.testcases.append(case(Input=[3, 15], Output=7.5))
		self.testcases.append(case(Input=[1,57], Output=76.50000))

	def get_testcases(self):
		return self.testcases
