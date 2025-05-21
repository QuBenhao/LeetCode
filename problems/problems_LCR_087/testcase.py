from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input="25525511135", Output=['255.255.11.135', '255.255.111.35']))
		self.testcases.append(case(Input="0000", Output=['0.0.0.0']))
		self.testcases.append(case(Input="1111", Output=['1.1.1.1']))
		self.testcases.append(case(Input="010010", Output=['0.10.0.10', '0.100.1.0']))
		self.testcases.append(case(Input="10203040", Output=['10.20.30.40', '102.0.30.40', '10.203.0.40']))
		self.testcases.append(case(Input="", Output=[]))

	def get_testcases(self):
		return self.testcases
