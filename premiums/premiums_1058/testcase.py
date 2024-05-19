from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['0.700', '2.800', '4.900'], 8], Output="1.000"))
		self.testcases.append(case(Input=[['1.500', '2.500', '3.500'], 10], Output="-1"))
		self.testcases.append(case(Input=[['1.500', '2.500', '3.500'], 9], Output="1.500"))

	def get_testcases(self):
		return self.testcases
