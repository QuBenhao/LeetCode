from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[3, 5, 2, 4], Output=2))
		self.testcases.append(case(Input=[9, 2, 5, 4], Output=4))
		self.testcases.append(case(Input=[7, 6, 8], Output=0))
		self.testcases.append(case(Input=[42,83,48,10,24,55,9,100,10,17,17,99,51,32,16,98,99,31,28,68,71,14,64,29,15,40], Output=26))

	def get_testcases(self):
		return self.testcases
