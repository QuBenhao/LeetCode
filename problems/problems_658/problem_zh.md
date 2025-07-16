# 658. 找到 K 个最接近的元素 

<p>给定一个 <strong>排序好</strong> 的数组&nbsp;<code>arr</code> ，两个整数 <code>k</code> 和 <code>x</code> ，从数组中找到最靠近 <code>x</code>（两数之差最小）的 <code>k</code> 个数。返回的结果必须要是按升序排好的。</p>

<p>整数 <code>a</code> 比整数 <code>b</code> 更接近 <code>x</code> 需要满足：</p>

<ul>
	<li><code>|a - x| &lt; |b - x|</code> 或者</li>
	<li><code>|a - x| == |b - x|</code> 且 <code>a &lt; b</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>arr = [1,2,3,4,5], k = 4, x = 3
<strong>输出：</strong>[1,2,3,4]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>arr = [1,1,2,3,4,5], k = 4, x = -1
<strong>输出：</strong>[1,1,2,3]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= arr.length</code></li>
	<li><code>1 &lt;= arr.length&nbsp;&lt;= 10<sup>4</sup></code><meta charset="UTF-8" /></li>
	<li><code>arr</code>&nbsp;按 <strong>升序</strong> 排列</li>
	<li><code>-10<sup>4</sup>&nbsp;&lt;= arr[i], x &lt;= 10<sup>4</sup></code></li>
</ul>
