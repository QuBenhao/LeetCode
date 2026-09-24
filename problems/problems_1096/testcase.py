from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="{a,b}{c,{d,e}}", Output=['ac', 'ad', 'ae', 'bc', 'bd', 'be']))
		self.testcases.append(case(Input="{{a,z},a{b,c},{ab,z}}", Output=['a', 'ab', 'ac', 'z']))

	def get_testcases(self):
		return self.testcases
