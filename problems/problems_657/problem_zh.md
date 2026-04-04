# 657. 机器人能否返回原点 

<p>在二维平面上，有一个机器人从原点 <code>(0, 0)</code> 开始。给出它的移动顺序，判断这个机器人在完成移动后是否在<strong>&nbsp;<code>(0, 0)</code> 处结束</strong>。</p>

<p>移动顺序由字符串&nbsp;<code>moves</code>&nbsp;表示。字符 <code>move[i]</code> 表示其第 <code>i</code> 次移动。机器人的有效动作有&nbsp;<code>R</code>（右），<code>L</code>（左），<code>U</code>（上）和 <code>D</code>（下）。</p>

<p>如果机器人在完成所有动作后返回原点，则返回 <code>true</code>。否则，返回 <code>false</code>。</p>

<p><strong>注意：</strong>机器人“面朝”的方向无关紧要。 <code>“R”</code> 将始终使机器人向右移动一次，<code>“L”</code> 将始终向左移动等。此外，假设每次移动机器人的移动幅度相同。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> moves = "UD"
<strong>输出:</strong> true
<strong>解释：</strong>机器人向上移动一次，然后向下移动一次。所有动作都具有相同的幅度，因此它最终回到它开始的原点。因此，我们返回 true。</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> moves = "LL"
<strong>输出:</strong> false
<strong>解释：</strong>机器人向左移动两次。它最终位于原点的左侧，距原点有两次 “移动” 的距离。我们返回 false，因为它在移动结束时没有返回原点。</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;= moves.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>moves</code>&nbsp;只包含字符&nbsp;<code>'U'</code>,&nbsp;<code>'D'</code>,&nbsp;<code>'L'</code>&nbsp;和&nbsp;<code>'R'</code></li>
</ul>
