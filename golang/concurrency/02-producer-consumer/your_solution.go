package main

type MySolution struct{}

// Solve
/**
2. 生产者-消费者模型
场景： 创建 3 个生产者协程和 2 个消费者协程：
	- 生产者每秒生成一个随机整数（1-100）
	- 消费者立即打印接收到的数字
	- 程序在 5 秒后自动终止

要求：
使用 context.Context 实现优雅关闭
避免 channel 泄漏
消费者打印需要显示消费者编号
*/
func (s *MySolution) Solve(timeout int, producers int, consumers int) {

}
