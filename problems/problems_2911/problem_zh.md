# 2911. 得到 K 个半回文串的最少修改次数 [难度分: 2607.94]

<p>给你一个字符串 <code>s</code> 和一个整数 <code>k</code>，请将 <code>s</code> 划分为 <code>k</code> 个&nbsp;<strong><span data-keyword="substring-nonempty">非空子串</span></strong>&nbsp;，使得将每个子串变为&nbsp;<strong>半回文串</strong>&nbsp;所需的字符修改次数之和最小。</p>

<p>返回所需的<em><strong>&nbsp;最少</strong>&nbsp;字符修改次数</em>。</p>

<p><strong>半回文串&nbsp;</strong>是一类特殊的字符串：它可以按照某种重复模式拆分后，使每一组都成为&nbsp;<strong><span data-keyword="palindrome">回文串</span></strong>&nbsp;。判断一个字符串是否为半回文串的方法如下：</p>

<ol>
	<li>选择该字符串长度的一个正因数 <code>d</code>。其中，<code>d</code> 的取值范围是从 <code>1</code> 到严格小于字符串长度的所有正因数。对于长度为 <code>1</code> 的字符串，根据这一定义，它不存在合法的因数，因为唯一的因数就是其长度本身，而这是不允许的。</li>
	<li>对于给定的因数 <code>d</code>，将字符串按长度为 <code>d</code> 的重复模式分组。具体来说，第 1 组由位置 <code>1</code>、<code>1 + d</code>、<code>1 + 2d</code>、…… 上的字符组成；第 2 组由位置 <code>2</code>、<code>2 + d</code>、<code>2 + 2d</code>、…… 上的字符组成；以此类推。</li>
	<li>如果这些分组中的每一组都是回文串，则该字符串被视为半回文串。</li>
</ol>

<p>以字符串 <code>"abcabc"</code> 为例：</p>

<ul>
	<li><code>"abcabc"</code> 的长度为 <code>6</code>。合法的因数有 <code>1</code>、<code>2</code> 和 <code>3</code>。</li>
	<li>当 <code>d = 1</code> 时：整个字符串 <code>"abcabc"</code> 构成一组。它不是回文串。</li>
	<li>当 <code>d = 2</code> 时：
	<ul>
		<li>第 1 组（位置 <code>1, 3, 5</code>）：<code>"acb"</code></li>
		<li>第 2 组（位置 <code>2, 4, 6</code>）：<code>"bac"</code></li>
		<li>这两组都不是回文串。</li>
	</ul>
	</li>
	<li>当 <code>d = 3</code> 时：
	<ul>
		<li>第 1 组（位置 <code>1, 4</code>）：<code>"aa"</code></li>
		<li>第 2 组（位置 <code>2, 5</code>）：<code>"bb"</code></li>
		<li>第 3 组（位置 <code>3, 6</code>）：<code>"cc"</code></li>
		<li>所有分组都是回文串。因此，<code>"abcabc"</code> 是一个半回文串。</li>
	</ul>
	</li>
</ul>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p><strong>输入：</strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> s = "abcac", k = 2 </span></p>

<p><strong>输出：</strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> 1 </span></p>

<p><strong>解释：</strong> 将 <code>s</code> 划分为 <code>"ab"</code> 和 <code>"cac"</code>。<code>"cac"</code> 本身已经是半回文串。将 <code>"ab"</code> 改为 <code>"aa"</code> 后，它在 <code>d = 1</code> 时成为半回文串。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p><strong>输入：</strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> s = "abcdef", k = 2 </span></p>

<p><strong>输出：</strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> 2 </span></p>

<p><strong>解释：</strong> 将其划分为子串 <code>"abc"</code> 和 <code>"def"</code>。这两个子串各自都需要修改 1 个字符才能变成半回文串。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
<p><strong>输入：</strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> s = "aabbaa", k = 3 </span></p>

<p><strong>输出：</strong> <span class="example-io" style="font-family: Menlo,sans-serif; font-size: 0.85rem;"> 0 </span></p>

<p><strong>解释：</strong> 将其划分为子串 <code>"aa"</code>、<code>"bb"</code> 和 <code>"aa"</code>。它们都已经是半回文串。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= s.length &lt;= 200</code></li>
	<li><code>1 &lt;= k &lt;= s.length / 2</code></li>
	<li><code>s</code> 仅由小写英文字母组成。</li>
</ul>
