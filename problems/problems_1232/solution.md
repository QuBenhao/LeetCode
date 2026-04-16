# [Python/Java/Golang/C++] 数学

> Author: Benhao
> Date: 2024-06-07
> Upvotes: 1
> Tags: C++, Go, Java, Python3

---


> Problem: [1232. 缀点成线](https://leetcode.cn/problems/check-if-it-is-a-straight-line/description/)


# Code
```Python3 []
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        """
        (y1 - y0) / (x1 - x0) = (y2 - y0) / (x2 - x0)
        y1x2 - y0x2 - y1x0 = y2x1 - y0x1 - y2x0
        x0y2 - x0y1 + x1y0 -x1y2 + x2y1 - x2y0 = 0
        (x1y0 - x0y1) + x2 * (y1 - y0) + y2 * (x0 - x1) = 0
        """
        yd, xd, c = (coordinates[1][1] - coordinates[0][1],
                     coordinates[1][0] - coordinates[0][0],
                     coordinates[0][0] * coordinates[1][1] - coordinates[0][1] * coordinates[1][0])
        for x, y in coordinates[2:]:
            if x * yd - y * xd != c:
                return False
        return True
```
```Golang []
func checkStraightLine(coordinates [][]int) bool {
	xd, yd, c := coordinates[1][0]-coordinates[0][0], coordinates[1][1]-coordinates[0][1],
		coordinates[0][0]*coordinates[1][1]-coordinates[1][0]*coordinates[0][1]
	for _, coordinate := range coordinates {
		x, y := coordinate[0], coordinate[1]
		if x*yd-y*xd != c {
			return false
		}
	}
	return true
}
```
```C++ []
class Solution {
public:
    bool checkStraightLine(vector<vector<int>>& coordinates) {
        int xd = coordinates[1][0] - coordinates[0][0], yd = coordinates[1][1] - coordinates[0][1];
        int c = coordinates[0][0] * coordinates[1][1] - coordinates[0][1] * coordinates[1][0];
        for (int i = 2; i < coordinates.size(); i++) {
            auto x = coordinates[i][0], y = coordinates[i][1];
            if (x * yd - y * xd != c) {
                return false;
            }
        }
        return true;
    }
};
```
```Java []
class Solution {
    public boolean checkStraightLine(int[][] coordinates) {
        int xd = coordinates[1][0] - coordinates[0][0], yd = coordinates[1][1] - coordinates[0][1],
                c = coordinates[0][0] * coordinates[1][1] - coordinates[0][1] * coordinates[1][0];
        for (int i = 2; i < coordinates.length; i++) {
            if (coordinates[i][0] * yd - coordinates[i][1] * xd != c) {
                return false;
            }
        }
        return true;
    }
}
```
  
