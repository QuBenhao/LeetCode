# 825. 适龄的朋友 [难度分: 1697.02]

<p>在社交媒体网站上有 <code>n</code> 个用户。给你一个整数数组 <code>ages</code> ，其中 <code>ages[i]</code> 是第 <code>i</code> 个用户的年龄。</p>

<p>如果下述任意一个条件为真，那么用户 <code>x</code> 将不会向用户 <code>y</code>（<code>x != y</code>）发送好友请求：</p>

<ul>
	<li><code>ages[y] &lt;= 0.5 * ages[x] + 7</code></li>
	<li><code>ages[y] &gt; ages[x]</code></li>
	<li><code>ages[y] &gt; 100 &amp;&amp; ages[x] &lt; 100</code></li>
</ul>

<p>否则，<code>x</code> 将会向 <code>y</code> 发送一条好友请求。</p>

<p>注意，如果 <code>x</code> 向 <code>y</code> 发送一条好友请求，<code>y</code> 不必也向 <code>x</code> 发送一条好友请求。另外，用户不会向自己发送好友请求。</p>

<p>返回在该社交媒体网站上产生的好友请求总数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>ages = [16,16]
<strong>输出：</strong>2
<strong>解释：</strong>2 人互发好友请求。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>ages = [16,17,18]
<strong>输出：</strong>2
<strong>解释：</strong>产生的好友请求为 17 -&gt; 16 ，18 -&gt; 17 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>ages = [20,30,100,110,120]
<strong>输出：</strong>3
<strong>解释：</strong>产生的好友请求为 110 -&gt; 100 ，120 -&gt; 110 ，120 -&gt; 100 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == ages.length</code></li>
	<li><code>1 &lt;= n &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= ages[i] &lt;= 120</code></li>
</ul>
