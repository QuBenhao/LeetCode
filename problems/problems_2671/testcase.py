from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['FrequencyTracker', 'add', 'add', 'hasFrequency'], [[], [3], [3], [2]]], Output=[None, None, None, True]))
		self.testcases.append(case(Input=[['FrequencyTracker', 'add', 'deleteOne', 'hasFrequency'], [[], [1], [1], [1]]], Output=[None, None, None, False]))
		self.testcases.append(case(Input=[['FrequencyTracker', 'hasFrequency', 'add', 'hasFrequency'], [[], [2], [3], [1]]], Output=[None, False, None, True]))
		self.testcases.append(case(Input=[["FrequencyTracker","add","add","hasFrequency","hasFrequency","add","add","add"], [[],[5],[5],[1],[2],[6],[5],[1]]], Output=[None,None,None,False,True,None,None,None]))

	def get_testcases(self):
		return self.testcases
