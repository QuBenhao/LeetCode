from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['08-15', '08-18', '08-16', '08-19'], Output=3))
		self.testcases.append(case(Input=['10-01', '10-31', '11-01', '12-31'], Output=0))

	def get_testcases(self):
		return self.testcases
