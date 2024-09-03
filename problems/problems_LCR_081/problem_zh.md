# LCR 081. 组合总和 

<p>给定一个<strong>无重复元素</strong>的正整数数组&nbsp;<code>candidates</code>&nbsp;和一个正整数&nbsp;<code>target</code>&nbsp;，找出&nbsp;<code>candidates</code>&nbsp;中所有可以使数字和为目标数&nbsp;<code>target</code>&nbsp;的唯一组合。</p>

<p><code>candidates</code>&nbsp;中的数字可以无限制重复被选取。如果至少一个所选数字数量不同，则两种组合是不同的。&nbsp;</p>

<p>对于给定的输入，保证和为&nbsp;<code>target</code> 的唯一组合数少于 <code>150</code> 个。</p>

<p>&nbsp;</p>

<p><strong>示例&nbsp;1：</strong></p>

<pre>
<strong>输入: </strong>candidates = [2,3,6,7], target = 7
<strong>输出: </strong>[[7],[2,2,3]]
</pre>

<p><strong>示例&nbsp;2：</strong></p>

<pre>
<strong>输入: </strong>candidates = [2,3,5], target = 8
<strong>输出: </strong>[[2,2,2,2],[2,3,3],[3,5]]</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入: </strong>candidates = [2], target = 1
<strong>输出: </strong>[]
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入: </strong>candidates = [1], target = 1
<strong>输出: </strong>[[1]]
</pre>

<p><strong>示例 5：</strong></p>

<pre>
<strong>输入: </strong>candidates = [1], target = 2
<strong>输出: </strong>[[1,1]]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= candidates.length &lt;= 30</code></li>
	<li><code>1 &lt;= candidates[i] &lt;= 200</code></li>
	<li><code>candidate</code> 中的每个元素都是独一无二的。</li>
	<li><code>1 &lt;= target &lt;= 500</code></li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 39&nbsp;题相同：&nbsp;<a href="https://leetcode-cn.com/problems/combination-sum/">https://leetcode-cn.com/problems/combination-sum/</a></p>
