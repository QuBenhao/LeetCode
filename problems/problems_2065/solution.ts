function maximalPathQuality(values: number[], edges: number[][], maxTime: number): number {
    const n = values.length;
    const g: number[][][] = Array.from({ length: n }, () => []);
    for (const edge of edges) {
        g[edge[0]].push([edge[1], edge[2]]);
        g[edge[1]].push([edge[0], edge[2]]);
    }

    const visited = new Array(n).fill(false);
    visited[0] = true;
    let ans = 0;
    const dfs = (u: number, time: number, value: number): void => {
        if (u === 0) {
            ans = Math.max(ans, value);
        }
        for (const [v, dist] of g[u]) {
            if (time + dist <= maxTime) {
                if (!visited[v]) {
                    visited[v] = true;
                    dfs(v, time + dist, value + values[v]);
                    visited[v] = false;
                } else {
                    dfs(v, time + dist, value);
                }
            }
        }
    };

    dfs(0, 0, values[0]);
    return ans;
};

export function Solve(inputJsonElement: string): any {
	const splits: string[] = inputJsonElement.split("\n");
	const values: number[] = JSON.parse(splits[0]);
	const edges: number[][] = JSON.parse(splits[1]);
	const maxTime: number = JSON.parse(splits[2]);
	return maximalPathQuality(values, edges, maxTime);
}
