# 3619. 可以被 K 整除的岛屿总价值数目 

<p>给你一个 <code>m x n</code> 的矩阵 <code>grid</code> 和一个正整数 <code>k</code>。一个&nbsp;<strong>岛屿&nbsp;</strong>是由&nbsp;<strong>正&nbsp;</strong>整数（表示陆地）组成的，并且陆地间&nbsp;<strong>四周&nbsp;</strong>连通（水平或垂直）。</p>

<p>一个岛屿的总价值是该岛屿中所有单元格的值之和。</p>

<p>返回总价值可以被 <code>k</code> <strong>整除&nbsp;</strong>的岛屿数量。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2025/03/06/example1griddrawio-1.png" style="width: 200px; height: 200px;" />
<div class="example-block">
<p><strong>输入:</strong> <span class="example-io">grid = [[0,2,1,0,0],[0,5,0,0,5],[0,0,1,0,0],[0,1,4,7,0],[0,2,0,0,8]], k = 5</span></p>

<p><strong>输出:</strong> <span class="example-io">2</span></p>

<p><strong>解释:</strong></p>

<p>网格中包含四个岛屿。蓝色高亮显示的岛屿的总价值可以被 5 整除，而红色高亮显示的岛屿则不能。</p>
</div>

<p><strong class="example">示例 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2025/03/06/example2griddrawio.png" style="width: 200px; height: 150px;" />
<div class="example-block">
<p><strong>输入:</strong> <span class="example-io">grid = [[3,0,3,0], [0,3,0,3], [3,0,3,0]], k = 3</span></p>

<p><strong>输出:</strong> <span class="example-io">6</span></p>

<p><strong>解释:</strong></p>

<p>网格中包含六个岛屿，每个岛屿的总价值都可以被 3 整除。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 1000</code></li>
	<li><code>1 &lt;= m * n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 10<sup>6</sup></code></li>
	<li><code>1 &lt;= k &lt; = 10<sup>6</sup></code></li>
</ul>
