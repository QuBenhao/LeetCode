from collections import namedtuple
import testcase

case = namedtuple("Testcase", ["Input", "Output"])


class Testcase(testcase.Testcase):
	def __init__(self):
		self.testcases = []
		self.testcases.append(case(Input=[['VideoSharingPlatform', 'upload', 'upload', 'remove', 'remove', 'upload', 'watch', 'watch', 'like', 'dislike', 'dislike', 'getLikesAndDislikes', 'getViews'], [[], ['123'], ['456'], [4], [0], ['789'], [1, 0, 5], [1, 0, 1], [1], [1], [1], [1], [1]]], Output=[None, 0, 1, None, None, 0, '456', '45', None, None, None, [1, 2], 2]))
		self.testcases.append(case(Input=[['VideoSharingPlatform', 'remove', 'watch', 'like', 'dislike', 'getLikesAndDislikes', 'getViews'], [[], [0], [0, 0, 1], [0], [0], [0], [0]]], Output=[None, None, '-1', None, None, [-1], -1]))

	def get_testcases(self):
		return self.testcases
