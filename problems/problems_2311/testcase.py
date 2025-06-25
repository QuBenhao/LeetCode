from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=['1001010', 5], Output=5))
		self.testcases.append(case(Input=['00101001', 1], Output=6))
		self.testcases.append(case(Input=["111100010000011101001110001111000000001011101111111110111000011111011000010101110100110110001111001001011001010011010000011111101001101000000101101001110110000111101011000101",11713332], Output=96))
		self.testcases.append(case(Input=["100110111111000000010011101000111011000001000111010001010111100001111110110010100011100100111000011011000000100001011000000100110110001101011010011",522399436], Output=92))

	def get_testcases(self):
		return self.testcases
