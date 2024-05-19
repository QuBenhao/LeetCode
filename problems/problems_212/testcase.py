from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[['o', 'a', 'a', 'n'], ['e', 't', 'a', 'e'], ['i', 'h', 'k', 'r'], ['i', 'f', 'l', 'v']], ['oath', 'pea', 'eat', 'rain']], Output=['eat', 'oath']))
		self.testcases.append(case(Input=[[['a', 'b'], ['c', 'd']], ['abcb']], Output=[]))

	def get_testcases(self):
		return self.testcases
