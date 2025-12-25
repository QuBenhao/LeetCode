//
// Created by benhao on 2025/12/24.
//

// #include<bits/stdc++.h>
#include <vector>
#include <iostream>
#define reg register int
#define MAXN 300010
using namespace std;
int n,m,head[MAXN],dis[MAXN],tot,maxx,bh,pre[MAXN],sumfr[MAXN],sumla[MAXN],num[MAXN],lian[MAXN],ans=2e9+7;
bool mark[MAXN],vis[MAXN];
struct node {
	int st,ed,lca,d;
} P[MAXN];
struct Edge {//前向星
	int ed,v,last;
} G[MAXN*2];
struct que {
	int ed,id;
};
vector<que> Q[MAXN];
struct s__ {//树剖预处理
	int son[MAXN],size[MAXN],top[MAXN],deep[MAXN];
	void DFS1(int x,int fa,int v) {
		dis[x]=dis[fa]+v;
		pre[x]=fa;
		deep[x]=deep[fa]+1;
		size[x]=1;
		for(int i=head[x]; ~i; i=G[i].last) {
			int t=G[i].ed,v=G[i].v;
			if(t==fa)continue;
			DFS1(t,x,v);
			size[x]+=size[t];
			if(size[son[x]]<size[t])son[x]=t;
		}
	}
	void DFS2(int x,int fa,int zu) {
		top[x]=zu;
		if(son[x])DFS2(son[x],x,zu);
		for(int i=head[x]; ~i; i=G[i].last) {
			int t=G[i].ed;
			if(t==son[x]||t==fa)continue;
			DFS2(t,x,t);
		}
	}
	int LCA(int x,int y) {
		while(top[x]!=top[y]) {
			if(deep[top[x]]<deep[top[y]])swap(x,y);
			x=pre[top[x]];
		}
		if(deep[x]>deep[y])swap(x,y);
		return x;
	}
} shupou;
void Rd(int &res) {//读优
	res=0;
	char ch=getchar();
	while('0'>ch||ch>'9')ch=getchar();
	while('0'<=ch&&ch<='9')res=(res<<3)+(res<<1)+(ch-'0'),ch=getchar();
}
void Add(int st,int ed,int v) {
	tot++;
	G[tot]=Edge {ed,v,head[st]};
	head[st]=tot;
}
void DFS(int x,int fa,int &bb) {
	num[x]=bb;
	for(int i=head[x]; ~i; i=G[i].last) {
		int t=G[i].ed;
		if(t==fa)continue;
		if(!mark[t])continue;
		lian[bb]=G[i].v;
		bb++;
		DFS(t,x,bb);
	}
}
void DFSla(int x,int fa,int zu) {//后缀
	vis[x]=1;
	for(int i=0; i<Q[x].size(); i++) {//访问vector
		int t=Q[x][i].ed,id=Q[x][i].id;
		if(vis[t]==1)sumla[zu]=max(sumla[zu],P[id].d);//更新
	}
	int nex=0;
	for(int i=head[x]; ~i; i=G[i].last) {
		int t=G[i].ed,v=G[i].v;
		if(t==fa)continue;
		if(mark[t]) {//优先遍历两旁伸出的子树
			nex=t;
			continue;
		}
		DFSla(t,x,zu);
	}
	if(nex) {
		sumla[num[nex]]=sumla[num[x]];//更新下一个的后缀
		if(nex==P[bh].st)return;//下一个点如果是另一端点的话就直接退出
		DFSla(nex,x,num[nex]);
	}
}
void DFSfr(int x,int fa,int zu) {//前缀
	vis[x]=1;
	for(int i=0; i<Q[x].size(); i++) {//访问vector
		int t=Q[x][i].ed,id=Q[x][i].id;
		if(vis[t]==1)sumfr[zu]=max(sumfr[zu],P[id].d);//更新
	}
	int nex=0;
	for(int i=head[x]; ~i; i=G[i].last) {
		int t=G[i].ed,v=G[i].v;
		if(t==fa)continue;
		if(mark[t]) {//优先遍历两旁伸出的子树
			nex=t;
			continue;
		}
		DFSfr(t,x,zu);
	}
	if(nex) {
		sumfr[num[nex]]=sumfr[num[x]];//更新下一个的前缀
		if(nex==P[bh].ed)return;//下一个点如果是另一端点的话就直接退出
		DFSfr(nex,x,num[nex]);
	}
}
int main() {
	memset(head,-1,sizeof(head));
	Rd(n),Rd(m);
	for(int i=1; i<=n-1; i++) {
		int x,y,z;
		Rd(x),Rd(y),Rd(z);
		Add(x,y,z);
		Add(y,x,z);
	}
	shupou.DFS1(1,0,0);
	shupou.DFS2(1,0,1);
	for(int i=1; i<=m; i++) {
		Rd(P[i].st),Rd(P[i].ed);
		P[i].lca=shupou.LCA(P[i].st,P[i].ed);
		P[i].d=dis[P[i].st]+dis[P[i].ed]-2*dis[P[i].lca];
		if(P[i].d>maxx)maxx=P[i].d,bh=i;
		Q[P[i].st].push_back(que {P[i].ed,i});
		Q[P[i].ed].push_back(que {P[i].st,i});
	}
	int st=P[bh].st,ed=P[bh].ed,lca=P[bh].lca;
	while(st!=lca)mark[st]=true,st=pre[st];
	while(ed!=lca)mark[ed]=true,ed=pre[ed];
	mark[lca]=true;
	int bb=1;
	DFS(P[bh].st,0,bb);
	DFSfr(P[bh].st,0,num[P[bh].st]);
	memset(vis,false,sizeof(vis));
	DFSla(P[bh].ed,0,num[P[bh].ed]);
	for(int i=1;i<=bb;i++){//更新最终答案
		int res=0;
		res=max(res,P[bh].d-lian[i]);
		res=max(res,sumfr[i]);
		res=max(res,sumla[i+1]);
		ans=min(ans,res);
	}
	cout<<ans;
	return 0;
}
