package main

type MySolution struct{}

// Solve
/**
8. 缓存击穿防护
场景：实现一个高并发缓存系统：
	- 当缓存失效时，确保只有一个协程去数据库加载数据
	- 其他协程等待该协程加载完成
	- 模拟 100 个并发请求同时到达缓存失效时刻

要求：
使用 sync.Once 或 singleflight 模式
添加随机加载耗时（100-500ms）
输出显示实际执行加载的次数
*/
func (s *MySolution) Solve(requests int) {

}
