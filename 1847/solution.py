import solution
import bisect, math


class Solution(solution.Solution):
    def solve(self, test_input=None):
        rooms, queries = test_input
        return self.closestRoom([x[:] for x in rooms], [x[:] for x in queries])

    def closestRoom(self, rooms, queries):
        """
        :type rooms: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        rooms.sort(key=lambda x: x[1], reverse=True)  # Sort by decreasing order of room size
        qArr = []  # zip query with its index
        for i, q in enumerate(queries):
            qArr.append((i, q))
        qArr.sort(key=lambda x: x[1][1], reverse=True)  # Sort by decreasing order of query minSize

        def searchGreaterOrEqual(arr, x):
            left = 0
            right = len(arr) - 1
            ans = -1
            while left <= right:
                mid = left + (right - left) // 2
                if arr[mid] >= x:
                    ans = mid
                    right = mid - 1
                else:
                    left = mid + 1
            return ans

        def searchLessOrEqual(arr, x):
            left = 0
            right = len(arr) - 1
            ans = -1
            while left <= right:
                mid = left + (right - left) // 2
                if arr[mid] <= x:
                    ans = mid
                    left = mid + 1
                else:
                    right = mid - 1
            return ans

        def binarySearch(arr, x):
            ansAbs = math.inf
            ans = -1
            i1 = searchGreaterOrEqual(arr, x)
            if i1 != -1:
                ansAbs = abs(x - arr[i1])
                ans = arr[i1]
            i2 = searchLessOrEqual(arr, x)
            if i2 != -1:
                if ansAbs >= abs(x - arr[i2]):
                    ans = arr[i2]
            return ans

        sortedRoomIdsSoFar = []  # Room id is sorted in
        n, k = len(rooms), len(queries)
        i = 0
        ans = [-1] * k
        for index, q in qArr:
            while i < n and rooms[i][1] >= q[1]:
                bisect.insort(sortedRoomIdsSoFar, rooms[i][0])  # Add id of the room which its size >= query minSize
                i += 1
            ans[index] = binarySearch(sortedRoomIdsSoFar, q[0])
        return ans
