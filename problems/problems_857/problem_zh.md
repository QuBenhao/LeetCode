# 857. 雇佣 K 名工人的最低成本 [难度分: 2259.66]

<p>有 <code>n</code>&nbsp;名工人。&nbsp;给定两个数组&nbsp;<code>quality</code>&nbsp;和&nbsp;<code>wage</code>&nbsp;，其中，<code>quality[i]</code>&nbsp;表示第&nbsp;<code>i</code>&nbsp;名工人的工作质量，其最低期望工资为&nbsp;<code>wage[i]</code>&nbsp;。</p>

<p>现在我们想雇佣&nbsp;<code>k</code>&nbsp;名工人组成一个&nbsp;<strong>工资组</strong><em>。</em>在雇佣&nbsp;一组 <code>k</code>&nbsp;名工人时，我们必须按照下述规则向他们支付工资：</p>

<ol>
	<li>对工资组中的每名工人，应当按其工作质量与同组其他工人的工作质量的比例来支付工资。</li>
	<li>工资组中的每名工人至少应当得到他们的最低期望工资。</li>
</ol>

<p>给定整数 <code>k</code> ，返回 <em>组成满足上述条件的付费群体所需的最小金额&nbsp;</em>。与实际答案误差相差在&nbsp;<code>10<sup>-5</sup></code>&nbsp;以内的答案将被接受。</p>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入： </strong>quality = [10,20,5], wage = [70,50,30], k = 2
<strong>输出： </strong>105.00000
<strong>解释：</strong> 我们向 0 号工人支付 70，向 2 号工人支付 35。</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入： </strong>quality = [3,1,10,10,1], wage = [4,8,2,2,7], k = 3
<strong>输出： </strong>30.66667
<strong>解释： </strong>我们向 0 号工人支付 4，向 2 号和 3 号分别支付 13.33333。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == quality.length == wage.length</code></li>
	<li><code>1 &lt;= k &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= quality[i], wage[i] &lt;= 10<sup>4</sup></code></li>
</ul>
