from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[[['a', 'b'], ['b', 'c']], [2.0, 3.0], [['a', 'c'], ['b', 'a'], ['a', 'e'], ['a', 'a'], ['x', 'x']]], Output=[6.0, 0.5, -1.0, 1.0, -1.0]))
		self.testcases.append(case(Input=[[['a', 'b'], ['b', 'c'], ['bc', 'cd']], [1.5, 2.5, 5.0], [['a', 'c'], ['c', 'b'], ['bc', 'cd'], ['cd', 'bc']]], Output=[3.75, 0.4, 5.0, 0.2]))
		self.testcases.append(case(Input=[[['a', 'b']], [0.5], [['a', 'b'], ['b', 'a'], ['a', 'c'], ['x', 'y']]], Output=[0.5, 2.0, -1.0, -1.0]))

	def get_testcases(self):
		return self.testcases
