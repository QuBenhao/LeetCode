# 2929. 给小朋友们分糖果 II [难度分: 1701.43]

<p>给你两个正整数&nbsp;<code>n</code> 和&nbsp;<code>limit</code>&nbsp;。</p>

<p>请你将 <code>n</code>&nbsp;颗糖果分给 <code>3</code>&nbsp;位小朋友，确保没有任何小朋友得到超过 <code>limit</code>&nbsp;颗糖果，请你返回满足此条件下的&nbsp;<strong>总方案数</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>n = 5, limit = 2
<b>输出：</b>3
<b>解释：</b>总共有 3 种方法分配 5 颗糖果，且每位小朋友的糖果数不超过 2 ：(1, 2, 2) ，(2, 1, 2) 和 (2, 2, 1) 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>n = 3, limit = 3
<b>输出：</b>10
<b>解释：</b>总共有 10 种方法分配 3 颗糖果，且每位小朋友的糖果数不超过 3 ：(0, 0, 3) ，(0, 1, 2) ，(0, 2, 1) ，(0, 3, 0) ，(1, 0, 2) ，(1, 1, 1) ，(1, 2, 0) ，(2, 0, 1) ，(2, 1, 0) 和 (3, 0, 0) 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>6</sup></code></li>
	<li><code>1 &lt;= limit &lt;= 10<sup>6</sup></code></li>
</ul>
