from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['London', 'New York'], ['New York', 'Lima'], ['Lima', 'Sao Paulo']], Output="Sao Paulo"))
		self.testcases.append(case(Input=[['B', 'C'], ['D', 'B'], ['C', 'A']], Output="A"))
		self.testcases.append(case(Input=[['A', 'Z']], Output="Z"))

	def get_testcases(self):
		return self.testcases
