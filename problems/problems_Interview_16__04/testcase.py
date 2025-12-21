from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['OX ', 'OX ', 'O  '], Output="X"))
		self.testcases.append(case(Input=['O'], Output="Draw"))
		self.testcases.append(case(Input=['OOXXOXXX', 'XXXOXOXO', 'OXOXXXOO', 'XOXOXXXX', 'OXOOXOOO', 'XOOOOOOO', 'OXXXOOOX', 'XOXOOXXX'], Output="Pending"))

	def get_testcases(self):
		return self.testcases
