# 1007. 行相等的最少多米诺旋转 [难度分: 1541.35]

<p>在一排多米诺骨牌中，<code>tops[i]</code> 和 <code>bottoms[i]</code>&nbsp;分别代表第 <code>i</code> 个多米诺骨牌的上半部分和下半部分。（一个多米诺是两个从 1 到 6 的数字同列平铺形成的&nbsp;—— 该平铺的每一半上都有一个数字。）</p>

<p>我们可以旋转第&nbsp;<code>i</code>&nbsp;张多米诺，使得 <code>tops[i]</code> 和 <code>bottoms[i]</code>&nbsp;的值交换。</p>

<p>返回能使 <code>tops</code> 中所有值或者 <code>bottoms</code> 中所有值都相同的最小旋转次数。</p>

<p>如果无法做到，返回&nbsp;<code>-1</code>.</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/14/domino.png" style="height: 300px; width: 421px;" />
<pre>
<strong>输入：</strong>tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
<strong>输出：</strong>2
<strong>解释：</strong> 
图一表示：在我们旋转之前， tops 和 bottoms 给出的多米诺牌。 
如果我们旋转第二个和第四个多米诺骨牌，我们可以使上面一行中的每个值都等于 2，如图二所示。 
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
<strong>输出：</strong>-1
<strong>解释：</strong> 在这种情况下，不可能旋转多米诺牌使一行的值相等。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= tops.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>bottoms.length == tops.length</code></li>
	<li><code>1 &lt;= tops[i], bottoms[i] &lt;= 6</code></li>
</ul>
