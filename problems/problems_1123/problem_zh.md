# 1123. 最深叶节点的最近公共祖先 [难度分: 1607.00]

<p>给你一个有根节点<meta charset="UTF-8" />&nbsp;<code>root</code>&nbsp;的二叉树，返回它&nbsp;<em>最深的叶节点的最近公共祖先</em>&nbsp;。</p>

<p>回想一下：</p>

<ul>
	<li><strong>叶节点</strong> 是二叉树中没有子节点的节点</li>
	<li>树的根节点的&nbsp;<strong>深度&nbsp;</strong>为&nbsp;<code>0</code>，如果某一节点的深度为&nbsp;<code>d</code>，那它的子节点的深度就是&nbsp;<code>d+1</code></li>
	<li>如果我们假定 <code>A</code> 是一组节点&nbsp;<code>S</code>&nbsp;的 <strong>最近公共祖先</strong>，<code>S</code>&nbsp;中的每个节点都在以 <code>A</code> 为根节点的子树中，且 <code>A</code>&nbsp;的深度达到此条件下可能的最大值。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/01/sketch1.png" style="height: 340px; width: 400px;" />
<pre>
<strong>输入：</strong>root = [3,5,1,6,2,0,8,null,null,7,4]
<strong>输出：</strong>[2,7,4]
<strong>解释：</strong>我们返回值为 2 的节点，在图中用黄色标记。
在图中用蓝色标记的是树的最深的节点。
注意，节点 6、0 和 8 也是叶节点，但是它们的深度是 2 ，而节点 7 和 4 的深度是 3 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>root = [1]
<strong>输出：</strong>[1]
<strong>解释：</strong>根节点是树中最深的节点，它是它本身的最近公共祖先。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>root = [0,1,3,null,2]
<strong>输出：</strong>[2]
<strong>解释：</strong>树中最深的叶节点是 2 ，最近公共祖先是它自己。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>树中的节点数将在<meta charset="UTF-8" />&nbsp;<code>[1, 1000]</code>&nbsp;的范围内。</li>
	<li><code>0 &lt;= Node.val &lt;= 1000</code></li>
	<li>每个节点的值都是&nbsp;<strong>独一无二</strong>&nbsp;的。</li>
</ul>

<p>&nbsp;</p>

<p><strong>注意：</strong>本题与力扣 865 重复：<a href="https://leetcode-cn.com/problems/smallest-subtree-with-all-the-deepest-nodes/">https://leetcode-cn.com/problems/smallest-subtree-with-all-the-deepest-nodes/</a></p>
