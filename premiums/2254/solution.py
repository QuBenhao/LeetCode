import solution
from typing import *
from object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = VideoSharingPlatform()
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]

class VideoSharingPlatform:

    def __init__(self):
        pass


    def upload(self, video: str) -> int:
            pass


    def remove(self, videoId: int) -> None:
            pass


    def watch(self, videoId: int, startMinute: int, endMinute: int) -> str:
                pass


    def like(self, videoId: int) -> None:
            pass


    def dislike(self, videoId: int) -> None:
            pass


    def getLikesAndDislikes(self, videoId: int) -> List[int]:
            pass


    def getViews(self, videoId: int) -> int:
            pass



# Your VideoSharingPlatform object will be instantiated and called as such:
# obj = VideoSharingPlatform()
# param_1 = obj.upload(video)
# obj.remove(videoId)
# param_3 = obj.watch(videoId,startMinute,endMinute)
# obj.like(videoId)
# obj.dislike(videoId)
# param_6 = obj.getLikesAndDislikes(videoId)
# param_7 = obj.getViews(videoId)