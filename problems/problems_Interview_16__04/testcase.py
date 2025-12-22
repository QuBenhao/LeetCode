from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=["O X"," XO","X O"], Output="X"))
		self.testcases.append(case(Input=["OOX","XXO","OXO"], Output="Draw"))
		self.testcases.append(case(Input=["OOX","XXO","OX "], Output="Pending"))
		self.testcases.append(case(Input=[" O    X"," O     ","     O ","XXXXXXX","  O    "," O   O ","O  X OO"], Output="X"))
		self.testcases.append(case(Input=["                             ","                     O       ","         X           X       ","                             ","                             ","                             ","                             ","                             ","                             ","                             ","                             ","                             ","                             ","                             ","                             ","                             ","                      O      ","                             ","                             ","                             ","                             ","                             ","                             ","      X                      ","                             ","                             ","      O                      ","                             ","                             "], Output="Pending"))

	def get_testcases(self):
		return self.testcases
