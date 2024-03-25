from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['SQL', 'insertRow', 'selectCell', 'insertRow', 'deleteRow', 'selectCell'], [[['one', 'two', 'three'], [2, 3, 1]], ['two', ['first', 'second', 'third']], ['two', 1, 3], ['two', ['fourth', 'fifth', 'sixth']], ['two', 1], ['two', 2, 2]]], Output=[None, None, 'third', None, None, 'fifth']))

	def get_testcases(self):
		return self.testcases
