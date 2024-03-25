from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="['4', '3d', '2r1', '2rd', '1o2', '1o1d', '1or1', '1ord', 'w3', 'w2d', 'w1r1', 'w1rd', 'wo2', 'wo1d', 'wor1', 'word']", Output=['4', '3d', '2r1', '2rd', '1o2', '1o1d', '1or1', '1ord', 'w3', 'w2d', 'w1r1', 'w1rd', 'wo2', 'wo1d', 'wor1', 'word']))
		self.testcases.append(case(Input="['1', 'a']", Output=['1', 'a']))

	def get_testcases(self):
		return self.testcases
