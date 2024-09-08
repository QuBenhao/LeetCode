# 2181. 合并零之间的节点 [难度分: 1333.19]

<p>给你一个链表的头节点 <code>head</code> ，该链表包含由 <code>0</code> 分隔开的一连串整数。链表的 <strong>开端</strong> 和 <strong>末尾</strong> 的节点都满足 <code>Node.val == 0</code> 。</p>

<p>对于每两个相邻的 <code>0</code> ，请你将它们之间的所有节点合并成一个节点，其值是所有已合并节点的值之和。然后将所有 <code>0</code> 移除，修改后的链表不应该含有任何 <code>0</code> 。</p>

<p>&nbsp;返回修改后链表的头节点 <code>head</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：<br />
<img alt="" src="https://assets.leetcode.com/uploads/2022/02/02/ex1-1.png" style="width: 600px; height: 41px;" /></strong></p>

<pre>
<strong>输入：</strong>head = [0,3,1,0,4,5,2,0]
<strong>输出：</strong>[4,11]
<strong>解释：</strong>
上图表示输入的链表。修改后的链表包含：
- 标记为绿色的节点之和：3 + 1 = 4
- 标记为红色的节点之和：4 + 5 + 2 = 11
</pre>

<p><strong>示例 2：<br />
<img alt="" src="https://assets.leetcode.com/uploads/2022/02/02/ex2-1.png" style="width: 600px; height: 41px;" /></strong></p>

<pre>
<strong>输入：</strong>head = [0,1,0,3,0,2,2,0]
<strong>输出：</strong>[1,3,4]
<strong>解释：</strong>
上图表示输入的链表。修改后的链表包含：
- 标记为绿色的节点之和：1 = 1
- 标记为红色的节点之和：3 = 3
- 标记为黄色的节点之和：2 + 2 = 4
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>列表中的节点数目在范围 <code>[3, 2 * 10<sup>5</sup>]</code> 内</li>
	<li><code>0 &lt;= Node.val &lt;= 1000</code></li>
	<li><strong>不</strong> 存在连续两个&nbsp;<code>Node.val == 0</code> 的节点</li>
	<li>链表的 <strong>开端</strong> 和 <strong>末尾</strong> 节点都满足 <code>Node.val == 0</code></li>
</ul>
