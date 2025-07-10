# 672. 灯泡开关 Ⅱ 

<p>房间中有 <code>n</code>&nbsp;只已经打开的灯泡，编号从 <code>1</code> 到 <code>n</code> 。墙上挂着 <strong>4 个开关</strong> 。</p>

<p>这 4 个开关各自都具有不同的功能，其中：</p>

<ul>
	<li><strong>开关 1 ：</strong>反转当前所有灯的状态（即开变为关，关变为开）</li>
	<li><strong>开关 2 ：</strong>反转编号为偶数的灯的状态（即 <code>0, 2, 4, ...</code>）</li>
	<li><strong>开关 3 ：</strong>反转编号为奇数的灯的状态（即 <code>1, 3, ...</code>）</li>
	<li><strong>开关 4 ：</strong>反转编号为 <code>j = 3k + 1</code> 的灯的状态，其中 <code>k = 0, 1, 2, ...</code>（即 <code>1, 4, 7, 10, ...</code>）</li>
</ul>

<p>你必须 <strong>恰好</strong> 按压开关 <code>presses</code> 次。每次按压，你都需要从 4 个开关中选出一个来执行按压操作。</p>

<p>给你两个整数 <code>n</code> 和 <code>presses</code> ，执行完所有按压之后，返回 <strong>不同可能状态</strong> 的数量。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 1, presses = 1
<strong>输出：</strong>2
<strong>解释：</strong>状态可以是：
- 按压开关 1 ，[关]
- 按压开关 2 ，[开]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 2, presses = 1
<strong>输出：</strong>3
<strong>解释：</strong>状态可以是：
- 按压开关 1 ，[关, 关]
- 按压开关 2 ，[开, 关]
- 按压开关 3 ，[关, 开]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 3, presses = 1
<strong>输出：</strong>4
<strong>解释：</strong>状态可以是：
- 按压开关 1 ，[关, 关, 关]
- 按压开关 2 ，[关, 开, 关]
- 按压开关 3 ，[开, 关, 开]
- 按压开关 4 ，[关, 开, 开]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
	<li><code>0 &lt;= presses &lt;= 1000</code></li>
</ul>
