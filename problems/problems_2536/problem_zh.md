# 2536. 子矩阵元素加 1 [难度分: 1583.31]

<p>给你一个正整数 <code>n</code> ，表示最初有一个 <code>n x n</code> 、下标从 <strong>0</strong> 开始的整数矩阵 <code>mat</code> ，矩阵中填满了 0 。</p>

<p>另给你一个二维整数数组 <code>query</code> 。针对每个查询 <code>query[i] = [row1<sub>i</sub>, col1<sub>i</sub>, row2<sub>i</sub>, col2<sub>i</sub>]</code> ，请你执行下述操作：</p>

<ul>
	<li>找出 <strong>左上角</strong> 为 <code>(row1<sub>i</sub>, col1<sub>i</sub>)</code> 且 <strong>右下角</strong> 为 <code>(row2<sub>i</sub>, col2<sub>i</sub>)</code> 的子矩阵，将子矩阵中的 <strong>每个元素</strong> 加 <code>1</code> 。也就是给所有满足 <code>row1<sub>i</sub> &lt;= x &lt;= row2<sub>i</sub></code> 和 <code>col1<sub>i</sub> &lt;= y &lt;= col2<sub>i</sub></code> 的 <code>mat[x][y]</code> 加 <code>1</code> 。</li>
</ul>

<p>返回执行完所有操作后得到的矩阵 <code>mat</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/11/24/p2example11.png" style="width: 531px; height: 121px;" /></p>

<pre>
<strong>输入：</strong>n = 3, queries = [[1,1,2,2],[0,0,1,1]]
<strong>输出：</strong>[[1,1,0],[1,2,1],[0,1,1]]
<strong>解释：</strong>上图所展示的分别是：初始矩阵、执行完第一个操作后的矩阵、执行完第二个操作后的矩阵。
- 第一个操作：将左上角为 (1, 1) 且右下角为 (2, 2) 的子矩阵中的每个元素加 1 。 
- 第二个操作：将左上角为 (0, 0) 且右下角为 (1, 1) 的子矩阵中的每个元素加 1 。 
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/11/24/p2example22.png" style="width: 261px; height: 82px;" /></p>

<pre>
<strong>输入：</strong>n = 2, queries = [[0,0,1,1]]
<strong>输出：</strong>[[1,1],[1,1]]
<strong>解释：</strong>上图所展示的分别是：初始矩阵、执行完第一个操作后的矩阵。 
- 第一个操作：将矩阵中的每个元素加 1 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 500</code></li>
	<li><code>1 &lt;= queries.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= row1<sub>i</sub> &lt;= row2<sub>i</sub> &lt; n</code></li>
	<li><code>0 &lt;= col1<sub>i</sub> &lt;= col2<sub>i</sub> &lt; n</code></li>
</ul>
