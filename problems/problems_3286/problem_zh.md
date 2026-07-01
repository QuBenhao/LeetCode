# 3286. 穿越网格图的安全路径 [难度分: 1607.82]

<p>给你一个&nbsp;<code>m x n</code>&nbsp;的二进制矩形&nbsp;<code>grid</code>&nbsp;和一个整数&nbsp;<code>health</code>&nbsp;表示你的健康值。</p>

<p>你开始于矩形的左上角&nbsp;<code>(0, 0)</code>&nbsp;，你的目标是矩形的右下角&nbsp;<code>(m - 1, n - 1)</code>&nbsp;。</p>

<p>你可以在矩形中往上下左右相邻格子移动，但前提是你的健康值始终是 <b>正数</b>&nbsp;。</p>

<p>对于格子&nbsp;<code>(i, j)</code>&nbsp;，如果&nbsp;<code>grid[i][j] = 1</code>&nbsp;，那么这个格子视为 <strong>不安全</strong>&nbsp;的，会使你的健康值减少 1 。</p>

<p>如果你可以到达最终的格子，请你返回&nbsp;<code>true</code>&nbsp;，否则返回 <code>false</code>&nbsp;。</p>

<p><b>注意</b>&nbsp;，当你在最终格子的时候，你的健康值也必须为<strong>&nbsp;正数</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]], health = 1</span></p>

<p><span class="example-io"><b>输出：</b>true</span></p>

<p><b>解释：</b></p>

<p>沿着下图中灰色格子走，可以安全到达最终的格子。</p>
<img alt="" src="https://assets.leetcode.com/uploads/2024/08/04/3868_examples_1drawio.png" style="width: 301px; height: 121px;" /></div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>grid = [[0,1,1,0,0,0],[1,0,1,0,0,0],[0,1,1,1,0,1],[0,0,1,0,1,0]], health = 3</span></p>

<p><span class="example-io"><b>输出：</b>false</span></p>

<p><b>解释：</b></p>

<p>健康值最少为 4 才能安全到达最后的格子。</p>
<img alt="" src="https://assets.leetcode.com/uploads/2024/08/04/3868_examples_2drawio.png" style="width: 361px; height: 161px;" /></div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>grid = [[1,1,1],[1,0,1],[1,1,1]], health = 5</span></p>

<p><span class="example-io"><b>输出：</b>true</span></p>

<p><b>解释：</b></p>

<p>沿着下图中灰色格子走，可以安全到达最终的格子。</p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/08/04/3868_examples_3drawio.png" style="width: 181px; height: 121px;" /></p>

<p>任何不经过格子&nbsp;<code>(1, 1)</code>&nbsp;的路径都是不安全的，因为你的健康值到达最终格子时，都会小于等于 0 。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 50</code></li>
<li><code>2 <= m * n</code></li>
	<li><code>1 &lt;= health &lt;= m + n</code></li>
	<li><code>grid[i][j]</code>&nbsp;要么是 0 ，要么是 1 。</li>
</ul>
