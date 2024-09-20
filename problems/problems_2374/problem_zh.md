# 2374. 边积分最高的节点 [难度分: 1418.98]

<p>给你一个有向图，图中有 <code>n</code> 个节点，节点编号从 <code>0</code> 到 <code>n - 1</code> ，其中每个节点都 <strong>恰有一条</strong> 出边。</p>

<p>图由一个下标从 <strong>0</strong> 开始、长度为 <code>n</code> 的整数数组 <code>edges</code> 表示，其中 <code>edges[i]</code> 表示存在一条从节点 <code>i</code> 到节点 <code>edges[i]</code> 的 <strong>有向</strong> 边。</p>

<p>节点 <code>i</code> 的 <strong>边积分</strong> 定义为：所有存在一条指向节点 <code>i</code> 的边的节点的 <strong>编号</strong> 总和。</p>

<p>返回 <strong>边积分</strong> 最高的节点。如果多个节点的 <strong>边积分</strong> 相同，返回编号 <strong>最小</strong> 的那个。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img src="https://assets.leetcode.com/uploads/2022/06/20/image-20220620195403-1.png" style="width: 450px; height: 260px;">
<pre><strong>输入：</strong>edges = [1,0,0,0,0,7,7,5]
<strong>输出：</strong>7
<strong>解释：</strong>
- 节点 1、2、3 和 4 都有指向节点 0 的边，节点 0 的边积分等于 1 + 2 + 3 + 4 = 10 。
- 节点 0 有一条指向节点 1 的边，节点 1 的边积分等于 0 。
- 节点 7 有一条指向节点 5 的边，节点 5 的边积分等于 7 。
- 节点 5 和 6 都有指向节点 7 的边，节点 7 的边积分等于 5 + 6 = 11 。
节点 7 的边积分最高，所以返回 7 。
</pre>

<p><strong>示例 2：</strong></p>
<img src="https://assets.leetcode.com/uploads/2022/06/20/image-20220620200212-3.png" style="width: 150px; height: 155px;">
<pre><strong>输入：</strong>edges = [2,0,0,2]
<strong>输出：</strong>0
<strong>解释：
</strong>- 节点 1 和 2 都有指向节点 0 的边，节点 0 的边积分等于 1 + 2 = 3 。
- 节点 0 和 3 都有指向节点 2 的边，节点 2 的边积分等于 0 + 3 = 3 。
节点 0 和 2 的边积分都是 3 。由于节点 0 的编号更小，返回 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == edges.length</code></li>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= edges[i] &lt; n</code></li>
	<li><code>edges[i] != i</code></li>
</ul>
