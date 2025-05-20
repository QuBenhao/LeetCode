package problem43

import (
	"encoding/json"
	"log"
	"strconv"
	"strings"
)

func multiply(num1 string, num2 string) string {
	if num1 == "0" || num2 == "0" {
		return "0"
	}
	res := make([]int, len(num1)+len(num2))
	for i := len(num1) - 1; i >= 0; i-- {
		n1 := int(num1[i] - '0')
		for j := len(num2) - 1; j >= 0; j-- {
			n2 := int(num2[j] - '0')
			cur := res[i+j+1] + n1*n2
			res[i+j+1] = cur % 10
			res[i+j] += cur / 10
		}
	}
	ans := ""
	for i := 0; i < len(res); i++ {
		if i == 0 && res[i] == 0 {
			continue
		}
		ans += strconv.Itoa(res[i])
	}
	return ans
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var num1 string
	var num2 string

	if err := json.Unmarshal([]byte(values[0]), &num1); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &num2); err != nil {
		log.Fatal(err)
	}

	return multiply(num1, num2)
}
