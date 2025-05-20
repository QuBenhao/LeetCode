package problem54

import (
	"encoding/json"
	"log"
	"strings"
)

func spiralOrder(matrix [][]int) (ans []int) {
	if matrix == nil || matrix[0] == nil {
		return
	}
	for left, right, top, bottom := 0, len(matrix[0])-1, 0, len(matrix)-1; left <= right && top <= bottom; {
		if left == right {
			for row := top; row <= bottom; row++ {
				ans = append(ans, matrix[row][left])
			}
			break
		}
		if top == bottom {
			for col := left; col <= right; col++ {
				ans = append(ans, matrix[top][col])
			}
			break
		}
		for col := left; col < right; col++ {
			ans = append(ans, matrix[top][col])
		}
		for row := top; row < bottom; row++ {
			ans = append(ans, matrix[row][right])
		}
		for col := right; col > left; col-- {
			ans = append(ans, matrix[bottom][col])
		}
		for row := bottom; row > top; row-- {
			ans = append(ans, matrix[row][left])
		}
		left, right, top, bottom = left+1, right-1, top+1, bottom-1
	}
	return
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var matrix [][]int

	if err := json.Unmarshal([]byte(values[0]), &matrix); err != nil {
		log.Fatal(err)
	}

	return spiralOrder(matrix)
}
