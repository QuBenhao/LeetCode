# 2322. 从树中删除边的最小分数 [难度分: 2391.66]

<p>存在一棵无向连通树，树中有编号从 <code>0</code> 到 <code>n - 1</code> 的 <code>n</code> 个节点， 以及 <code>n - 1</code> 条边。</p>

<p>给你一个下标从 <strong>0</strong> 开始的整数数组 <code>nums</code> ，长度为 <code>n</code> ，其中 <code>nums[i]</code> 表示第 <code>i</code> 个节点的值。另给你一个二维整数数组 <code>edges</code> ，长度为 <code>n - 1</code> ，其中 <code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> 表示树中存在一条位于节点 <code>a<sub>i</sub></code> 和 <code>b<sub>i</sub></code> 之间的边。</p>

<p>删除树中两条 <strong>不同</strong> 的边以形成三个连通组件。对于一种删除边方案，定义如下步骤以计算其分数：</p>

<ol>
	<li>分别获取三个组件 <strong>每个</strong> 组件中所有节点值的异或值。</li>
	<li><strong>最大</strong> 异或值和 <strong>最小</strong> 异或值的 <strong>差值</strong> 就是这一种删除边方案的分数。</li>
</ol>

<ul>
	<li>例如，三个组件的节点值分别是：<code>[4,5,7]</code>、<code>[1,9]</code> 和 <code>[3,3,3]</code> 。三个异或值分别是 <code>4 ^ 5 ^ 7 = <em><strong>6</strong></em></code>、<code>1 ^ 9 = <em><strong>8</strong></em></code> 和 <code>3 ^ 3 ^ 3 = <em><strong>3</strong></em></code> 。最大异或值是 <code>8</code> ，最小异或值是 <code>3</code> ，分数是 <code>8 - 3 = 5</code> 。</li>
</ul>

<p>返回在给定树上执行任意删除边方案可能的 <strong>最小</strong> 分数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/05/03/ex1drawio.png" style="width: 193px; height: 190px;">
<pre><strong>输入：</strong>nums = [1,5,5,4,11], edges = [[0,1],[1,2],[1,3],[3,4]]
<strong>输出：</strong>9
<strong>解释：</strong>上图展示了一种删除边方案。
- 第 1 个组件的节点是 [1,3,4] ，值是 [5,4,11] 。异或值是 5 ^ 4 ^ 11 = 10 。
- 第 2 个组件的节点是 [0] ，值是 [1] 。异或值是 1 = 1 。
- 第 3 个组件的节点是 [2] ，值是 [5] 。异或值是 5 = 5 。
分数是最大异或值和最小异或值的差值，10 - 1 = 9 。
可以证明不存在分数比 9 小的删除边方案。
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/05/03/ex2drawio.png" style="width: 287px; height: 150px;">
<pre><strong>输入：</strong>nums = [5,5,2,4,4,2], edges = [[0,1],[1,2],[5,2],[4,3],[1,3]]
<strong>输出：</strong>0
<strong>解释：</strong>上图展示了一种删除边方案。
- 第 1 个组件的节点是 [3,4] ，值是 [4,4] 。异或值是 4 ^ 4 = 0 。
- 第 2 个组件的节点是 [1,0] ，值是 [5,5] 。异或值是 5 ^ 5 = 0 。
- 第 3 个组件的节点是 [2,5] ，值是 [2,2] 。异或值是 2 ^ 2 = 0 。
分数是最大异或值和最小异或值的差值，0 - 0 = 0 。
无法获得比 0 更小的分数 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>3 &lt;= n &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>8</sup></code></li>
	<li><code>edges.length == n - 1</code></li>
	<li><code>edges[i].length == 2</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt; n</code></li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
	<li><code>edges</code> 表示一棵有效的树</li>
</ul>
