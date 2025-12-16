# 面试题 05.01. 插入 

<p>给定两个整型数字 <code>N</code> 与 <code>M</code>，以及表示比特位置的 <code>i</code> 与 <code>j</code>（<code>i &lt;= j</code>，且从 0 位开始计算）。</p>

<p>编写一种方法，使 <code>M</code> 对应的二进制数字插入 <code>N</code> 对应的二进制数字的第 <code>i ~ j</code> 位区域，不足之处用 <code>0</code> 补齐。具体插入过程如图所示。</p>

<p><img alt="" src="https://pic.leetcode.cn/1610104070-NuLVQi-05.01.gif" style="width: 267px; height: 200px;" /></p>

<p>题目保证从 <code>i</code> 位到 <code>j</code> 位足以容纳 <code>M</code>， 例如： <code>M = 10011</code>，则 <code>i～j</code> 区域至少可容纳 5 位。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong> 输入</strong>：N = 1024(10000000000), M = 19(10011), i = 2, j = 6
<strong> 输出</strong>：N = 1100(10001001100)
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong> 输入</strong>：N = 0, M = 31(11111), i = 0, j = 4
<strong> 输出</strong>：N = 31(11111)
</pre>
