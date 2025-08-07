# 808. 分汤 [难度分: 2396.63]

<p>你有两种汤，<strong>A</strong> 和 <strong>B</strong>，每种初始为 <code>n</code>&nbsp;毫升。在每一轮中，会随机选择以下四种服务操作中的一种，每种操作的概率为 <code>0.25</code>，且与之前的所有轮次 <strong>无关</strong>：</p>

<ol>
	<li>从汤 A 取 100 毫升，从汤 B 取 0 毫升</li>
	<li>从汤 A 取 75 毫升，从汤 B 取 25 毫升</li>
	<li>从汤 A 取 50 毫升，从汤 B 取 50 毫升</li>
	<li>从汤 A 取 25 毫升，从汤 B 取 75 毫升</li>
</ol>

<p><strong>注意：</strong></p>

<ul>
	<li>不存在先分配 <code>100</code> ml <strong>汤B</strong> 的操作。</li>
	<li>汤 A 和 B 在每次操作中同时被倒入。</li>
	<li>如果一次操作要求你倒出比剩余的汤更多的量，请倒出该汤剩余的所有部分。</li>
</ul>

<p>操作过程在任何回合中任一汤被用完后立即停止。</p>

<p>返回汤 A 在 B 前耗尽的概率，加上两种汤在 <strong>同一回合&nbsp;</strong>耗尽概率的一半。返回值在正确答案&nbsp;<code>10<sup>-5</sup></code>&nbsp;的范围内将被认为是正确的。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入：</strong>n = 50
<strong>输出：</strong>0.62500
<strong>解释：
</strong>如果我们选择前两个操作<strong>，</strong>A 首先将变为空。
对于第三个操作，A 和 B 会同时变为空。
对于第四个操作，B 首先将变为空。<strong>
</strong>所以 A 变为空的总概率加上 A 和 B 同时变为空的概率的一半是 0.25 *(1 + 1 + 0.5 + 0)= 0.625。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入：</strong>n = 100
<strong>输出：</strong>0.71875
<strong>解释：</strong>
如果我们选择第一个操作，A 首先将变为空。
如果我们选择第二个操作，A 将在执行操作 [1, 2, 3] 时变为空，然后 A 和 B 在执行操作 4 时同时变空。
如果我们选择第三个操作，A 将在执行操作 [1, 2] 时变为空，然后 A 和 B 在执行操作 3 时同时变空。
如果我们选择第四个操作，A 将在执行操作 1 时变为空，然后 A 和 B 在执行操作 2 时同时变空。
所以 A 变为空的总概率加上 A 和 B 同时变为空的概率的一半是 0.71875。
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 10<sup>9</sup></code></li>
</ul>
