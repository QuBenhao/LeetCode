from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="abcde", Output=5))
		self.testcases.append(case(Input="xyzxyzxyzxyz", Output=12))
		self.testcases.append(case(Input="aabbccddeeffgghhiiiiii", Output=24))

	def get_testcases(self):
		return self.testcases
