# 3249. 统计好节点的数目 [难度分: 1565.80]

<p>现有一棵 <strong>无向</strong> 树，树中包含 <code>n</code> 个节点，按从 <code>0</code> 到 <code>n - 1</code> 标记。树的根节点是节点 <code>0</code> 。给你一个长度为 <code>n - 1</code> 的二维整数数组 <code>edges</code>，其中 <code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> 表示树中节点 <code>a<sub>i</sub></code> 与节点 <code>b<sub>i</sub></code> 之间存在一条边。</p>

<p>如果一个节点的所有子节点为根的&nbsp;<span data-keyword="subtree">子树</span>&nbsp;包含的节点数相同，则认为该节点是一个 <strong>好节点</strong>。</p>

<p>返回给定树中<strong> 好节点 </strong>的数量。</p>

<p><strong>子树</strong>&nbsp;指的是一个节点以及它所有后代节点构成的一棵树。</p>

<p>&nbsp;</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]</span></p>

<p><strong>输出：</strong><span class="example-io">7</span></p>

<p><strong>说明：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2024/05/26/tree1.png" style="width: 360px; height: 158px;" />
<p>树的所有节点都是好节点。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">edges = [[0,1],[1,2],[2,3],[3,4],[0,5],[1,6],[2,7],[3,8]]</span></p>

<p><strong>输出：</strong><span class="example-io">6</span></p>

<p><strong>说明：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2024/06/03/screenshot-2024-06-03-193552.png" style="width: 360px; height: 303px;" />
<p>树中有 6 个好节点。上图中已将这些节点着色。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>edges = [[0,1],[1,2],[1,3],[1,4],[0,5],[5,6],[6,7],[7,8],[0,9],[9,10],[9,12],[10,11]]</span></p>

<p><span class="example-io"><b>输出：</b>12</span></p>

<p><strong>解释：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2024/08/08/rob.jpg" style="width: 450px; height: 277px;" />
<p>除了节点 9 以外其他所有节点都是好节点。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>edges.length == n - 1</code></li>
	<li><code>edges[i].length == 2</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt; n</code></li>
	<li>输入确保 <code>edges</code> 总表示一棵有效的树。</li>
</ul>
