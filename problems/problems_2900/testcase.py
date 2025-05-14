from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[["e","a","b"], [0,0,1]], Output=['e', 'b']))
		self.testcases.append(case(Input=[["a","b","c","d"], [1,0,1,1]], Output=['a', 'b', 'c']))

	def get_testcases(self):
		return self.testcases
