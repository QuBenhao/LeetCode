# 572. 另一棵树的子树 

<div class="original__bRMd">
<div>
<p>给你两棵二叉树 <code>root</code> 和 <code>subRoot</code> 。检验 <code>root</code> 中是否包含和 <code>subRoot</code> 具有相同结构和节点值的子树。如果存在，返回 <code>true</code> ；否则，返回 <code>false</code> 。</p>

<p>二叉树 <code>tree</code> 的一棵子树包括 <code>tree</code> 的某个节点和这个节点的所有后代节点。<code>tree</code> 也可以看做它自身的一棵子树。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/28/subtree1-tree.jpg" style="width: 532px; height: 400px;" />
<pre>
<strong>输入：</strong>root = [3,4,5,1,2], subRoot = [4,1,2]
<strong>输出：</strong>true
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/28/subtree2-tree.jpg" style="width: 502px; height: 458px;" />
<pre>
<strong>输入：</strong>root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
<strong>输出：</strong>false
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>root</code> 树上的节点数量范围是 <code>[1, 2000]</code></li>
	<li><code>subRoot</code> 树上的节点数量范围是 <code>[1, 1000]</code></li>
	<li><code>-10<sup>4</sup> <= root.val <= 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> <= subRoot.val <= 10<sup>4</sup></code></li>
</ul>
</div>
</div>
