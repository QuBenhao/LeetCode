function minimumDistance(points: number[][]): number {
    const n: number = points.length;
    const sx = [];
    const sy = [];
    for (let i = 0; i < n; i++) {
        const [x, y] = points[i];
        sx.push([x - y, i]);
        sy.push([x + y, i]);
    }
    sx.sort((a, b) => a[0] - b[0]);
    sy.sort((a, b) => a[0] - b[0]);
    const maxVal1: number = sx[n - 1][0] - sx[0][0];
    const maxVal2: number = sy[n - 1][0] - sy[0][0];
    let res: number = Infinity;
    if (maxVal1 >= maxVal2) {
        const i: number = sx[0][1], j: number = sx[n - 1][1];
        // 去掉 i 后的最大曼哈顿距离
        res = Math.min(res, Math.max(remove(sx, i), remove(sy, i)));
        // 去掉 j 后的最大曼哈顿距离
        res = Math.min(res, Math.max(remove(sx, j), remove(sy, j)));
    } else {
        const i: number = sy[0][1], j: number = sy[n - 1][1];
        // 去掉 i 后的最大曼哈顿距离
        res = Math.min(res, Math.max(remove(sx, i), remove(sy, i)));
        // 去掉 j 后的最大曼哈顿距离
        res = Math.min(res, Math.max(remove(sx, j), remove(sy, j)));
    }
    return res;
};

function remove(arr: [number, number][], i: number): number {
    const n: number = arr.length;
    if (arr[0][1] === i) {
        return arr[n - 1][0] - arr[1][0];
    } else if (arr[n - 1][1] === i) {
        return arr[n - 2][0] - arr[0][0];
    } else {
        return arr[n - 1][0] - arr[0][0];
    }
}

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const points: number[][] = JSON.parse(inputValues[0]);
	return minimumDistance(points);
}
