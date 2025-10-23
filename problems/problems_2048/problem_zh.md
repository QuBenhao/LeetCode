# 2048. 下一个更大的数值平衡数 [难度分: 1734.06]

<p>如果整数&nbsp; <code>x</code> 满足：对于每个数位&nbsp;<code>d</code> ，这个数位&nbsp;<strong>恰好</strong> 在 <code>x</code> 中出现 <code>d</code> 次。那么整数 <code>x</code> 就是一个 <strong>数值平衡数</strong> 。</p>

<p>给你一个整数 <code>n</code> ，请你返回 <strong>严格大于</strong> <code>n</code> 的 <strong>最小数值平衡数</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 1
<strong>输出：</strong>22
<strong>解释：</strong>
22 是一个数值平衡数，因为：
- 数字 2 出现 2 次 
这也是严格大于 1 的最小数值平衡数。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 1000
<strong>输出：</strong>1333
<strong>解释：</strong>
1333 是一个数值平衡数，因为：
- 数字 1 出现 1 次。
- 数字 3 出现 3 次。 
这也是严格大于 1000 的最小数值平衡数。
注意，1022 不能作为本输入的答案，因为数字 0 的出现次数超过了 0 。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 3000
<strong>输出：</strong>3133
<strong>解释：</strong>
3133 是一个数值平衡数，因为：
- 数字 1 出现 1 次。
- 数字 3 出现 3 次。 
这也是严格大于 3000 的最小数值平衡数。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 10<sup>6</sup></code></li>
</ul>
