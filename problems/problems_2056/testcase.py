from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['rook'], [[1, 1]]], Output=15))
		self.testcases.append(case(Input=[['queen'], [[1, 1]]], Output=22))
		self.testcases.append(case(Input=[['bishop'], [[4, 3]]], Output=12))
		self.testcases.append(case(Input=[["queen","bishop"],[[5,7],[3,4]]], Output=281))
		self.testcases.append(case(Input=[["rook","rook"],[[1,1],[8,8]]], Output=223))

	def get_testcases(self):
		return self.testcases
