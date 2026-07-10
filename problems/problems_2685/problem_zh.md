# 2685. 统计完全连通分量的数量 [难度分: 1769.43]

<p>给你一个整数 <code>n</code> 。现有一个包含 <code>n</code> 个顶点的 <strong>无向</strong> 图，顶点按从 <code>0</code> 到 <code>n - 1</code> 编号。给你一个二维整数数组 <code>edges</code> 其中 <code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> 表示顶点 <code>a<sub>i</sub></code> 和 <code>b<sub>i</sub></code> 之间存在一条 <strong>无向</strong> 边。</p>

<p>返回图中 <strong>完全连通分量</strong> 的数量。</p>

<p>如果在子图中任意两个顶点之间都存在路径，并且子图中没有任何一个顶点与子图外部的顶点共享边，则称其为 <strong>连通分量</strong> 。</p>

<p>如果连通分量中每对节点之间都存在一条边，则称其为 <strong>完全连通分量</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2023/04/11/screenshot-from-2023-04-11-23-31-23.png" style="width: 671px; height: 270px;" /></strong></p>

<pre>
<strong>输入：</strong>n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]
<strong>输出：</strong>3
<strong>解释：</strong>如上图所示，可以看到此图所有分量都是完全连通分量。
</pre>

<p><strong>示例 2：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2023/04/11/screenshot-from-2023-04-11-23-32-00.png" style="width: 671px; height: 270px;" /></strong></p>

<pre>
<strong>输入：</strong>n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
<strong>输出：</strong>1
<strong>解释：</strong>包含节点 0、1 和 2 的分量是完全连通分量，因为每对节点之间都存在一条边。
包含节点 3 、4 和 5 的分量不是完全连通分量，因为节点 4 和 5 之间不存在边。
因此，在图中完全连接分量的数量是 1 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 50</code></li>
	<li><code>0 &lt;= edges.length &lt;= n * (n - 1) / 2</code></li>
	<li><code>edges[i].length == 2</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt;= n - 1</code></li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
	<li>不存在重复的边</li>
</ul>
