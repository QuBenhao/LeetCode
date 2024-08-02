# 2850. 将石头分散到网格图的最少移动次数 [难度分: 2001.45]

<p>给你一个大小为 <code>3 * 3</code>&nbsp;，下标从 <strong>0</strong>&nbsp;开始的二维整数矩阵&nbsp;<code>grid</code>&nbsp;，分别表示每一个格子里石头的数目。网格图中总共恰好有&nbsp;<code>9</code>&nbsp;个石头，一个格子里可能会有 <strong>多个</strong>&nbsp;石头。</p>

<p>每一次操作中，你可以将一个石头从它当前所在格子移动到一个至少有一条公共边的相邻格子。</p>

<p>请你返回每个格子恰好有一个石头的 <strong>最少移动次数</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2023/08/23/example1-3.svg" style="width: 401px; height: 281px;" /></p>

<pre>
<b>输入：</b>grid = [[1,1,0],[1,1,1],[1,2,1]]
<b>输出：</b>3
<b>解释：</b>让每个格子都有一个石头的一个操作序列为：
1 - 将一个石头从格子 (2,1) 移动到 (2,2) 。
2 - 将一个石头从格子 (2,2) 移动到 (1,2) 。
3 - 将一个石头从格子 (1,2) 移动到 (0,2) 。
总共需要 3 次操作让每个格子都有一个石头。
让每个格子都有一个石头的最少操作次数为 3 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2023/08/23/example2-2.svg" style="width: 401px; height: 281px;" /></p>

<pre>
<b>输入：</b>grid = [[1,3,0],[1,0,0],[1,0,3]]
<b>输出：</b>4
<b>解释：</b>让每个格子都有一个石头的一个操作序列为：
1 - 将一个石头从格子 (0,1) 移动到 (0,2) 。
2 - 将一个石头从格子 (0,1) 移动到 (1,1) 。
3 - 将一个石头从格子 (2,2) 移动到 (1,2) 。
4 - 将一个石头从格子 (2,2) 移动到 (2,1) 。
总共需要 4 次操作让每个格子都有一个石头。
让每个格子都有一个石头的最少操作次数为 4 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>grid.length == grid[i].length == 3</code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 9</code></li>
	<li><code>grid</code>&nbsp;中元素之和为&nbsp;<code>9</code> 。</li>
</ul>
