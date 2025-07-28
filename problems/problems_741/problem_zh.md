# 741. 摘樱桃 

<p>给你一个 <code>n x n</code> 的网格 <code>grid</code> ，代表一块樱桃地，每个格子由以下三种数字的一种来表示：</p>

<ul>
	<li><code>0</code> 表示这个格子是空的，所以你可以穿过它。</li>
	<li><code>1</code> 表示这个格子里装着一个樱桃，你可以摘到樱桃然后穿过它。</li>
	<li><code>-1</code> 表示这个格子里有荆棘，挡着你的路。</li>
</ul>

<p>请你统计并返回：在遵守下列规则的情况下，能摘到的最多樱桃数：</p>

<ul>
	<li>从位置&nbsp;<code>(0, 0)</code> 出发，最后到达 <code>(n - 1, n - 1)</code> ，只能向下或向右走，并且只能穿越有效的格子（即只可以穿过值为 <code>0</code> 或者 <code>1</code> 的格子）；</li>
	<li>当到达 <code>(n - 1, n&nbsp;- 1)</code> 后，你要继续走，直到返回到 <code>(0, 0) </code>，只能向上或向左走，并且只能穿越有效的格子；</li>
	<li>当你经过一个格子且这个格子包含一个樱桃时，你将摘到樱桃并且这个格子会变成空的（值变为 <code>0</code> ）；</li>
	<li>如果在 <code>(0, 0)</code> 和 <code>(n - 1, n - 1)</code> 之间不存在一条可经过的路径，则无法摘到任何一个樱桃。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/14/grid.jpg" />
<pre>
<b>输入：</b>grid = [[0,1,-1],[1,0,-1],[1,1,1]]
<b>输出：</b>5
<b>解释：</b>玩家从 (0, 0) 出发：向下、向下、向右、向右移动至 (2, 2) 。
在这一次行程中捡到 4 个樱桃，矩阵变成 [[0,1,-1],[0,0,-1],[0,0,0]] 。
然后，玩家向左、向上、向上、向左返回起点，再捡到 1 个樱桃。
总共捡到 5 个樱桃，这是最大可能值。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>grid = [[1,1,-1],[1,-1,1],[-1,1,1]]
<b>输出：</b>0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= n &lt;= 50</code></li>
	<li><code>grid[i][j]</code>&nbsp;为&nbsp;<code>-1</code>、<code>0</code>&nbsp;或&nbsp;<code>1</code></li>
	<li><code>grid[0][0] != -1</code></li>
	<li><code>grid[n - 1][n - 1] != -1</code></li>
</ul>
