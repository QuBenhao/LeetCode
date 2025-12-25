# 2483. 商店的最少代价 [难度分: 1494.50]

<p>给你一个顾客访问商店的日志，用一个下标从 <strong>0</strong>&nbsp;开始且只包含字符&nbsp;<code>'N'</code> 和&nbsp;<code>'Y'</code>&nbsp;的字符串&nbsp;<code>customers</code>&nbsp;表示：</p>

<ul>
	<li>如果第&nbsp;<code>i</code>&nbsp;个字符是&nbsp;<code>'Y'</code>&nbsp;，它表示第&nbsp;<code>i</code>&nbsp;小时有顾客到达。</li>
	<li>如果第&nbsp;<code>i</code>&nbsp;个字符是&nbsp;<code>'N'</code>&nbsp;，它表示第 <code>i</code>&nbsp;小时没有顾客到达。</li>
</ul>

<p>如果商店在第&nbsp;<code>j</code>&nbsp;小时关门（<code>0 &lt;= j &lt;= n</code>），代价按如下方式计算：</p>

<ul>
	<li>在开门期间，如果某一个小时没有顾客到达，代价增加 <code>1</code>&nbsp;。</li>
	<li>在关门期间，如果某一个小时有顾客到达，代价增加&nbsp;<code>1</code>&nbsp;。</li>
</ul>

<p>请你返回在确保代价 <strong>最小</strong>&nbsp;的前提下，商店的&nbsp;<strong>最早</strong>&nbsp;关门时间。</p>

<p>注意，商店在第 <code>j</code>&nbsp;小时关门表示在第 <code>j</code> 小时以及之后商店处于关门状态。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>customers = "YYNY"
<b>输出：</b>2
<b>解释：</b>
- 第 0 小时关门，总共 1+1+0+1 = 3 代价。
- 第 1 小时关门，总共 0+1+0+1 = 2 代价。
- 第 2 小时关门，总共 0+0+0+1 = 1 代价。
- 第 3 小时关门，总共 0+0+1+1 = 2 代价。
- 第 4 小时关门，总共 0+0+1+0 = 1 代价。
在第 2 或第 4 小时关门代价都最小。由于第 2 小时更早，所以最优关门时间是 2 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>customers = "NNNNN"
<b>输出：</b>0
<b>解释：</b>最优关门时间是 0 ，因为自始至终没有顾客到达。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>customers = "YYYY"
<b>输出：</b>4
<b>解释：</b>最优关门时间是 4 ，因为每一小时均有顾客到达。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= customers.length &lt;= 10<sup>5</sup></code></li>
	<li><code>customers</code>&nbsp;只包含字符&nbsp;<code>'Y'</code>&nbsp;和&nbsp;<code>'N'</code>&nbsp;。</li>
</ul>
