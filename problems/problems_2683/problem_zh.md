# 2683. 相邻值的按位异或 [难度分: 1517.83]

<p>下标从 <strong>0</strong> 开始、长度为 <code>n</code> 的数组 <code>derived</code> 是由同样长度为 <code>n</code> 的原始 <strong>二进制数组</strong> <code>original</code> 通过计算相邻值的 <strong>按位异或（⊕）</strong>派生而来。</p>

<p>特别地，对于范围&nbsp;<code>[0, n - 1]</code> 内的每个下标 <code>i</code> ：</p>

<ul>
	<li>如果 <code>i = n - 1</code> ，那么 <code>derived[i] = original[i] ⊕ original[0]</code></li>
	<li>否则 <code>derived[i] = original[i] ⊕ original[i + 1]</code></li>
</ul>

<p>给你一个数组 <code>derived</code> ，请判断是否存在一个能够派生得到 <code>derived</code> 的 <strong>有效原始二进制数组</strong> <code>original</code> 。</p>

<p>如果存在满足要求的原始二进制数组，返回 <em><strong>true</strong> </em>；否则，返回<em> <strong>false</strong> </em>。</p>

<ul>
	<li>二进制数组是仅由 <strong>0</strong> 和 <strong>1</strong> 组成的数组。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>derived = [1,1,0]
<strong>输出：</strong>true
<strong>解释：</strong>能够派生得到 [1,1,0] 的有效原始二进制数组是 [0,1,0] ：
derived[0] = original[0] ⊕ original[1] = 0 ⊕ 1 = 1 
derived[1] = original[1] ⊕ original[2] = 1 ⊕ 0 = 1
derived[2] = original[2] ⊕ original[0] = 0 ⊕ 0 = 0
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>derived = [1,1]
<strong>输出：</strong>true
<strong>解释：</strong>能够派生得到 [1,1] 的有效原始二进制数组是 [0,1] ：
derived[0] = original[0] ⊕ original[1] = 1
derived[1] = original[1] ⊕ original[0] = 1
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>derived = [1,0]
<strong>输出：</strong>false
<strong>解释：</strong>不存在能够派生得到 [1,0] 的有效原始二进制数组。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == derived.length</code></li>
	<li><code>1 &lt;= n&nbsp;&lt;= 10<sup>5</sup></code></li>
	<li><code>derived</code> 中的值不是 <strong>0</strong> 就是 <strong>1</strong> 。</li>
</ul>
