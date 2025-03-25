# 2829. k-avoiding 数组的最小总和 [难度分: 1347.21]

<p>给你两个整数 <code>n</code> 和 <code>k</code> 。</p>

<p>对于一个由 <strong>不同</strong> 正整数组成的数组，如果其中不存在任何求和等于 k 的不同元素对，则称其为 <strong>k-avoiding</strong> 数组。</p>

<p>返回长度为 <code>n</code> 的 <strong>k-avoiding</strong> 数组的可能的最小总和。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 5, k = 4
<strong>输出：</strong>18
<strong>解释：</strong>设若 k-avoiding 数组为 [1,2,4,5,6] ，其元素总和为 18 。
可以证明不存在总和小于 18 的 k-avoiding 数组。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 2, k = 6
<strong>输出：</strong>3
<strong>解释：</strong>可以构造数组 [1,2] ，其元素总和为 3 。
可以证明不存在总和小于 3 的 k-avoiding 数组。 
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n, k &lt;= 50</code></li>
</ul>
