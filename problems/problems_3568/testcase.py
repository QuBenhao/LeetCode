from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['S.', 'XL'], 2], Output=2))
		self.testcases.append(case(Input=[['LS', 'RL'], 4], Output=3))
		self.testcases.append(case(Input=[['L.S', 'RXL'], 3], Output=-1))

	def get_testcases(self):
		return self.testcases
