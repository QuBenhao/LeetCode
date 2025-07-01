# 3331. 修改后子树的大小 [难度分: 2045.99]

<p>给你一棵 <code>n</code>&nbsp;个节点且根节点为编号 0 的树，节点编号为&nbsp;<code>0</code>&nbsp;到&nbsp;<code>n - 1</code>&nbsp;。这棵树用一个长度为&nbsp;<code>n</code>&nbsp;的数组&nbsp;<code>parent</code>&nbsp;表示，其中&nbsp;<code>parent[i]</code>&nbsp;是第 <code>i</code>&nbsp;个节点的父亲节点的编号。由于节点 0 是根，<code>parent[0] == -1</code>&nbsp;。</p>

<p>给你一个长度为 <code>n</code>&nbsp;的字符串&nbsp;<code>s</code>&nbsp;，其中&nbsp;<code>s[i]</code>&nbsp;是节点 <code>i</code>&nbsp;对应的字符。</p>

<p>对于节点编号从 <code>1</code>&nbsp;到 <code>n - 1</code>&nbsp;的每个节点 <code>x</code>&nbsp;，我们 <strong>同时</strong> 执行以下操作 <strong>一次</strong>&nbsp;：</p>

<ul>
	<li>找到距离节点 <code>x</code>&nbsp;<strong>最近</strong>&nbsp;的祖先节点 <code>y</code>&nbsp;，且&nbsp;<code>s[x] == s[y]</code>&nbsp;。</li>
	<li>如果节点 <code>y</code>&nbsp;不存在，那么不做任何修改。</li>
	<li>否则，将节点 <code>x</code>&nbsp;与它父亲节点之间的边 <strong>删除</strong>&nbsp;，在 <code>x</code>&nbsp;与 <code>y</code>&nbsp;之间连接一条边，使&nbsp;<code>y</code>&nbsp;变为 <code>x</code>&nbsp;新的父节点。</li>
</ul>

<p>请你返回一个长度为 <code>n</code>&nbsp;的数组&nbsp;<code>answer</code>&nbsp;，其中&nbsp;<code>answer[i]</code>&nbsp;是 <strong>最终</strong>&nbsp;树中，节点 <code>i</code>&nbsp;为根的 <span data-keyword="subtree">子树</span> 的 <strong>大小</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>parent = [-1,0,0,1,1,1], s = "abaabc"</span></p>

<p><span class="example-io"><b>输出：</b>[6,3,1,1,1,1]</span></p>

<p><strong>解释：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/08/15/graphex1drawio.png" style="width: 230px; height: 277px;" /></p>

<p>节点 3 的父节点从节点 1 变为节点 0 。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>parent = [-1,0,4,0,1], s = "abbba"</span></p>

<p><span class="example-io"><b>输出：</b>[5,2,1,1,1]</span></p>

<p><b>解释：</b></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/08/20/exgraph2drawio.png" style="width: 160px; height: 308px;" /></p>

<p>以下变化会同时发生：</p>

<ul>
	<li>节点 4 的父节点从节点 1 变为节点 0 。</li>
	<li>节点 2 的父节点从节点 4 变为节点 1 。</li>
</ul>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == parent.length == s.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li>对于所有的&nbsp;<code>i &gt;= 1</code>&nbsp;，都有&nbsp;<code>0 &lt;= parent[i] &lt;= n - 1</code>&nbsp;。</li>
	<li><code>parent[0] == -1</code></li>
	<li><code>parent</code>&nbsp;表示一棵合法的树。</li>
	<li><code>s</code>&nbsp;只包含小写英文字母。</li>
</ul>
