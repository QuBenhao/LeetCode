from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="fabccddg", Output=3))
		self.testcases.append(case(Input="abababaccddb", Output=2))

	def get_testcases(self):
		return self.testcases
