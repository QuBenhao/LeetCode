from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['ValidWordAbbr', 'isUnique', 'isUnique', 'isUnique', 'isUnique', 'isUnique'], [[['deer', 'door', 'cake', 'card']], ['dear'], ['cart'], ['cane'], ['make'], ['cake']]], Output=[None, False, True, False, True, True]))

	def get_testcases(self):
		return self.testcases
