package problem1863

import (
	"encoding/json"
	"log"
	"strings"
)

func subsetXORSum(nums []int) int {
	/*
		异或: 每位比特位可以独立看待，相互互不影响

		假设某位比特位，有m个1，有n-m个0
		那么异或结果为1的子集数就是:
		1. 选1个1，n-m里的全部子集 -- Cm_1 * 2^(n-m)
		2. 选3个1, n-m里的全部子集 -- Cm_3 * 2^(n-m)
		...
		2^(n-m) * (Cm_1 + Cm_3 + Cm_5 + ...)

		由于奇数的组合数和等于偶数的组合数和, 上面的式子等价于:
		2^(n-m) * 2^(m-1) = 2^(n-1)

		所以每位为1的影响是2^(n-1)，整体就是或的结果再出现2^(n-1)次
	*/
	or := 0
	for _, num := range nums {
		or |= num
	}
	return or << (len(nums) - 1)
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return subsetXORSum(nums)
}
