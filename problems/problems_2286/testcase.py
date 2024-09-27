from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['BookMyShow', 'gather', 'gather', 'scatter', 'scatter'], [[2, 5], [4, 0], [2, 0], [5, 1], [5, 1]]], Output=[None, [0, 0], [], True, False]))

	def get_testcases(self):
		return self.testcases
