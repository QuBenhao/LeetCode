# 2385. 感染二叉树需要的总时间 [难度分: 1711.49]

<p>给你一棵二叉树的根节点 <code>root</code> ，二叉树中节点的值 <strong>互不相同</strong> 。另给你一个整数 <code>start</code> 。在第 <code>0</code> 分钟，<strong>感染</strong> 将会从值为 <code>start</code> 的节点开始爆发。</p>

<p>每分钟，如果节点满足以下全部条件，就会被感染：</p>

<ul>
	<li>节点此前还没有感染。</li>
	<li>节点与一个已感染节点相邻。</li>
</ul>

<p>返回感染整棵树需要的分钟数<em>。</em></p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/06/25/image-20220625231744-1.png" style="width: 400px; height: 306px;">
<pre><strong>输入：</strong>root = [1,5,3,null,4,10,6,9,2], start = 3
<strong>输出：</strong>4
<strong>解释：</strong>节点按以下过程被感染：
- 第 0 分钟：节点 3
- 第 1 分钟：节点 1、10、6
- 第 2 分钟：节点5
- 第 3 分钟：节点 4
- 第 4 分钟：节点 9 和 2
感染整棵树需要 4 分钟，所以返回 4 。
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/06/25/image-20220625231812-2.png" style="width: 75px; height: 66px;">
<pre><strong>输入：</strong>root = [1], start = 1
<strong>输出：</strong>0
<strong>解释：</strong>第 0 分钟，树中唯一一个节点处于感染状态，返回 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>树中节点的数目在范围 <code>[1, 10<sup>5</sup>]</code> 内</li>
	<li><code>1 &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
	<li>每个节点的值 <strong>互不相同</strong></li>
	<li>树中必定存在值为 <code>start</code> 的节点</li>
</ul>
