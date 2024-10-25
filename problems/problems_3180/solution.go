package problem3180

import (
	"encoding/json"
	"log"
	"math/big"
	"slices"
	"strings"
)

func maxTotalReward(rewardValues []int) int {
	slices.Sort(rewardValues)
	rewardValues = slices.Compact(rewardValues) // 去重

	one := big.NewInt(1)
	f := big.NewInt(1)
	p := new(big.Int)
	for _, v := range rewardValues {
		mask := p.Sub(p.Lsh(one, uint(v)), one)
		f.Or(f, p.Lsh(p.And(f, mask), uint(v)))
	}
	return f.BitLen() - 1
}


func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var rewardValues []int

	if err := json.Unmarshal([]byte(inputValues[0]), &rewardValues); err != nil {
		log.Fatal(err)
	}

	return maxTotalReward(rewardValues)
}
