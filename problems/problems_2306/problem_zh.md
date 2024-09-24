# 2306. 公司命名 [难度分: 2305.45]

<p>给你一个字符串数组 <code>ideas</code> 表示在公司命名过程中使用的名字列表。公司命名流程如下：</p>

<ol>
	<li>从 <code>ideas</code> 中选择 2 个 <strong>不同</strong> 名字，称为 <code>idea<sub>A</sub></code> 和 <code>idea<sub>B</sub></code> 。</li>
	<li>交换 <code>idea<sub>A</sub></code> 和 <code>idea<sub>B</sub></code> 的首字母。</li>
	<li>如果得到的两个新名字 <strong>都</strong> 不在 <code>ideas</code> 中，那么 <code>idea<sub>A</sub> idea<sub>B</sub></code>（<strong>串联</strong> <code>idea<sub>A</sub></code> 和 <code>idea<sub>B</sub></code> ，中间用一个空格分隔）是一个有效的公司名字。</li>
	<li>否则，不是一个有效的名字。</li>
</ol>

<p>返回 <strong>不同</strong> 且有效的公司名字的数目。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>ideas = ["coffee","donuts","time","toffee"]
<strong>输出：</strong>6
<strong>解释：</strong>下面列出一些有效的选择方案：
- ("coffee", "donuts")：对应的公司名字是 "doffee conuts" 。
- ("donuts", "coffee")：对应的公司名字是 "conuts doffee" 。
- ("donuts", "time")：对应的公司名字是 "tonuts dime" 。
- ("donuts", "toffee")：对应的公司名字是 "tonuts doffee" 。
- ("time", "donuts")：对应的公司名字是 "dime tonuts" 。
- ("toffee", "donuts")：对应的公司名字是 "doffee tonuts" 。
因此，总共有 6 个不同的公司名字。

下面列出一些无效的选择方案：
- ("coffee", "time")：在原数组中存在交换后形成的名字 "toffee" 。
- ("time", "toffee")：在原数组中存在交换后形成的两个名字。
- ("coffee", "toffee")：在原数组中存在交换后形成的两个名字。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>ideas = ["lack","back"]
<strong>输出：</strong>0
<strong>解释：</strong>不存在有效的选择方案。因此，返回 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= ideas.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= ideas[i].length &lt;= 10</code></li>
	<li><code>ideas[i]</code> 由小写英文字母组成</li>
	<li><code>ideas</code> 中的所有字符串 <strong>互不相同</strong></li>
</ul>
