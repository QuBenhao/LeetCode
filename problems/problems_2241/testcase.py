from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['ATM', 'deposit', 'withdraw', 'deposit', 'withdraw', 'withdraw'], [[], [[0, 0, 1, 2, 1]], [600], [[0, 1, 0, 1, 1]], [600], [550]]], Output=[None, None, [0, 0, 1, 0, 1], None, [-1], [0, 1, 0, 0, 1]]))
		self.testcases.append(case(Input=[["ATM","deposit","withdraw"],[[],[[0,10,0,3,0]],[500]]], Output=[None,None,[0,2,0,2,0]]))

	def get_testcases(self):
		return self.testcases
