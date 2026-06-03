from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[120, 130], Output=3))
		self.testcases.append(case(Input=[198, 202], Output=3))
		self.testcases.append(case(Input=[4848, 4848], Output=2))

	def get_testcases(self):
		return self.testcases
