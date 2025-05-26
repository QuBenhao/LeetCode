package main

import (
	"fmt"
	"sync"
)

/**
1. 基础协程同步
场景：实现一个函数并发计算 10 个数字的平方，主协程等待所有计算完成后输出结果。
要求：
使用 sync.WaitGroup 实现协程同步
禁止使用全局变量
输出顺序不需要保证
*/

func main() {
	var wg sync.WaitGroup
	numbers := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	for _, n := range numbers {
		wg.Add(1) // 在每个 goroutine 开始前增加计数
		go func(num int) {
			// 使用匿名函数来捕获变量 n
			square := num * num
			fmt.Printf("Square of %d is %d\n", num, square)
			wg.Done() // 在每个 goroutine 完成后减少计数
		}(n)
	}
	// 等待所有 goroutine 完成
	wg.Wait()
}
