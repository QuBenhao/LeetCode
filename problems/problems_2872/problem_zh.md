# 2872. 可以被 K 整除连通块的最大数目 [难度分: 1967.56]

<p>给你一棵 <code>n</code>&nbsp;个节点的无向树，节点编号为&nbsp;<code>0</code>&nbsp;到&nbsp;<code>n - 1</code>&nbsp;。给你整数&nbsp;<code>n</code>&nbsp;和一个长度为 <code>n - 1</code>&nbsp;的二维整数数组&nbsp;<code>edges</code>&nbsp;，其中&nbsp;<code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code>&nbsp;表示树中节点&nbsp;<code>a<sub>i</sub></code> 和&nbsp;<code>b<sub>i</sub></code>&nbsp;有一条边。</p>

<p>同时给你一个下标从 <strong>0</strong>&nbsp;开始长度为 <code>n</code>&nbsp;的整数数组&nbsp;<code>values</code>&nbsp;，其中&nbsp;<code>values[i]</code>&nbsp;是第 <code>i</code>&nbsp;个节点的 <strong>值</strong>&nbsp;。再给你一个整数&nbsp;<code>k</code>&nbsp;。</p>

<p>你可以从树中删除一些边，也可以一条边也不删，得到若干连通块。一个 <strong>连通块的值</strong> 定义为连通块中所有节点值之和。如果所有连通块的值都可以被 <code>k</code>&nbsp;整除，那么我们说这是一个 <strong>合法分割</strong>&nbsp;。</p>

<p>请你返回所有合法分割中，<b>连通块数目的最大值</b>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2023/08/07/example12-cropped2svg.jpg" style="width: 1024px; height: 453px;" /></p>

<pre>
<b>输入：</b>n = 5, edges = [[0,2],[1,2],[1,3],[2,4]], values = [1,8,1,4,4], k = 6
<b>输出：</b>2
<b>解释：</b>我们删除节点 1 和 2 之间的边。这是一个合法分割，因为：
- 节点 1 和 3 所在连通块的值为 values[1] + values[3] = 12 。
- 节点 0 ，2 和 4 所在连通块的值为 values[0] + values[2] + values[4] = 6 。
最多可以得到 2 个连通块的合法分割。</pre>

<p><strong class="example">示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2023/08/07/example21svg-1.jpg" style="width: 999px; height: 338px;" /></p>

<pre>
<b>输入：</b>n = 7, edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], values = [3,0,6,1,5,2,1], k = 3
<b>输出：</b>3
<b>解释：</b>我们删除节点 0 和 2 ，以及节点 0 和 1 之间的边。这是一个合法分割，因为：
- 节点 0 的连通块的值为 values[0] = 3 。
- 节点 2 ，5 和 6 所在连通块的值为 values[2] + values[5] + values[6] = 9 。
- 节点 1 ，3 和 4 的连通块的值为 values[1] + values[3] + values[4] = 6 。
最多可以得到 3 个连通块的合法分割。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>edges.length == n - 1</code></li>
	<li><code>edges[i].length == 2</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt; n</code></li>
	<li><code>values.length == n</code></li>
	<li><code>0 &lt;= values[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>9</sup></code></li>
	<li><code>values</code>&nbsp;之和可以被 <code>k</code>&nbsp;整除。</li>
	<li>输入保证&nbsp;<code>edges</code>&nbsp;是一棵无向树。</li>
</ul>
