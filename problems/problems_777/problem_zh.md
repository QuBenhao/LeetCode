# 777. 在 LR 字符串中交换相邻字符 [难度分: 1938.69]

<p>在一个由 <code>'L'</code> , <code>'R'</code> 和 <code>'X'</code> 三个字符组成的字符串（例如<code>"RXXLRXRXL"</code>）中进行移动操作。一次移动操作指用一个&nbsp;<code>"LX"</code>&nbsp;替换一个&nbsp;<code>"XL"</code>，或者用一个&nbsp;<code>"XR"</code>&nbsp;替换一个&nbsp;<code>"RX"</code>。现给定起始字符串&nbsp;<code>start</code>&nbsp;和结束字符串&nbsp;<code>result</code>，请编写代码，当且仅当存在一系列移动操作使得&nbsp;<code>start</code>&nbsp;可以转换成&nbsp;<code>result</code>&nbsp;时， 返回&nbsp;<code>True</code>。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>start = "RXXLRXRXL", result = "XRLXXRRLX"
<strong>输出：</strong>true
<strong>解释：</strong>通过以下步骤我们可以将 start 转化为 result：
RXXLRXRXL -&gt;
XRXLRXRXL -&gt;
XRLXRXRXL -&gt;
XRLXXRRXL -&gt;
XRLXXRRLX
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>start = "X", result = "L"
<strong>输出：</strong>false
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= start.length&nbsp;&lt;= 10<sup>4</sup></code></li>
	<li><code>start.length == result.length</code></li>
	<li><code>start</code> 和&nbsp;<code>result</code>&nbsp;都只包含&nbsp;<code>'L'</code>, <code>'R'</code>&nbsp;或&nbsp;<code>'X'</code>。</li>
</ul>
