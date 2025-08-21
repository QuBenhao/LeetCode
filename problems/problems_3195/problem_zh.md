# 3195. 包含所有 1 的最小矩形面积 I [难度分: 1348.50]

<p>给你一个二维 <strong>二进制 </strong>数组 <code>grid</code>。请你找出一个边在水平方向和竖直方向上、面积 <strong>最小</strong> 的矩形，并且满足 <code>grid</code> 中所有的 1 都在矩形的内部。</p>

<p>返回这个矩形可能的 <strong>最小 </strong>面积。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">grid = [[0,1,0],[1,0,1]]</span></p>

<p><strong>输出：</strong> <span class="example-io">6</span></p>

<p><strong>解释：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/05/08/examplerect0.png" style="padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem; width: 279px; height: 198px;" /></p>

<p>这个最小矩形的高度为 2，宽度为 3，因此面积为 <code>2 * 3 = 6</code>。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">grid = [[0,0],[1,0]]</span></p>

<p><strong>输出：</strong> <span class="example-io">1</span></p>

<p><strong>解释：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/05/08/examplerect1.png" style="padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem; width: 204px; height: 201px;" /></p>

<p>这个最小矩形的高度和宽度都是 1，因此面积为 <code>1 * 1 = 1</code>。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= grid.length, grid[i].length &lt;= 1000</code></li>
	<li><code>grid[i][j]</code> 是 0 或 1。</li>
	<li>输入保证 <code>grid</code> 中至少有一个 1 。</li>
</ul>
