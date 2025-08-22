# 3197. 包含所有 1 的最小矩形面积 II [难度分: 2540.77]

<p>给你一个二维 <strong>二进制 </strong>数组 <code>grid</code>。你需要找到 3 个<strong> 不重叠</strong>、面积 <strong>非零</strong> 、边在水平方向和竖直方向上的矩形，并且满足 <code>grid</code> 中所有的 1 都在这些矩形的内部。</p>

<p>返回这些矩形面积之和的<strong> 最小 </strong>可能值。</p>

<p><strong>注意</strong>，这些矩形可以相接。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">grid = [[1,0,1],[1,1,1]]</span></p>

<p><strong>输出：</strong> <span class="example-io">5</span></p>

<p><strong>解释：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/05/14/example0rect21.png" style="padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem; width: 280px; height: 198px;" /></p>

<ul>
	<li>位于 <code>(0, 0)</code> 和 <code>(1, 0)</code> 的 1 被一个面积为 2 的矩形覆盖。</li>
	<li>位于 <code>(0, 2)</code> 和 <code>(1, 2)</code> 的 1 被一个面积为 2 的矩形覆盖。</li>
	<li>位于 <code>(1, 1)</code> 的 1 被一个面积为 1 的矩形覆盖。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">grid = [[1,0,1,0],[0,1,0,1]]</span></p>

<p><strong>输出：</strong> <span class="example-io">5</span></p>

<p><strong>解释：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/05/14/example1rect2.png" style="padding: 10px; background: rgb(255, 255, 255); border-radius: 0.5rem; width: 356px; height: 198px;" /></p>

<ul>
	<li>位于 <code>(0, 0)</code> 和 <code>(0, 2)</code> 的 1 被一个面积为 3 的矩形覆盖。</li>
	<li>位于 <code>(1, 1)</code> 的 1 被一个面积为 1 的矩形覆盖。</li>
	<li>位于 <code>(1, 3)</code> 的 1 被一个面积为 1 的矩形覆盖。</li>
</ul>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= grid.length, grid[i].length &lt;= 30</code></li>
	<li><code>grid[i][j]</code> 是 0 或 1。</li>
	<li>输入保证 <code>grid</code> 中至少有三个 1 。</li>
</ul>
