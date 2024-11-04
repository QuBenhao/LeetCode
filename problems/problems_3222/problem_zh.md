# 3222. 求出硬币游戏的赢家 [难度分: 1269.96]

<p>给你两个 <strong>正</strong>&nbsp;整数&nbsp;<code>x</code>&nbsp;和&nbsp;<code>y</code>&nbsp;，分别表示价值为 75 和 10 的硬币的数目。</p>

<p>Alice 和 Bob 正在玩一个游戏。每一轮中，Alice&nbsp;先进行操作，Bob 后操作。每次操作中，玩家需要拿出价值 <b>总和</b>&nbsp;为 115 的硬币。如果一名玩家无法执行此操作，那么这名玩家 <strong>输掉</strong>&nbsp;游戏。</p>

<p>两名玩家都采取 <strong>最优</strong>&nbsp;策略，请你返回游戏的赢家。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>x = 2, y = 7</span></p>

<p><span class="example-io"><b>输出：</b>"Alice"</span></p>

<p><strong>解释：</strong></p>

<p>游戏一次操作后结束：</p>

<ul>
	<li>Alice 拿走 1 枚价值为 75 的硬币和 4 枚价值为 10 的硬币。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>x = 4, y = 11</span></p>

<p><span class="example-io"><b>输出：</b>"Bob"</span></p>

<p><strong>解释：</strong></p>

<p>游戏 2 次操作后结束：</p>

<ul>
	<li>Alice 拿走&nbsp;1 枚价值为 75 的硬币和 4 枚价值为 10 的硬币。</li>
	<li>Bob 拿走&nbsp;1 枚价值为 75 的硬币和 4 枚价值为 10 的硬币。</li>
</ul>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= x, y &lt;= 100</code></li>
</ul>
