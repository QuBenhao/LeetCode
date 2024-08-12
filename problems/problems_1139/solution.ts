function largest1BorderedSquare(grid: number[][]): number {
    const m: number = grid.length, n: number = grid[0].length;
    const preRow: Array<Array<number>> = new Array(m).fill(0).map(() => new Array(n + 1).fill(0));
    const preCol: Array<Array<number>> = new Array(n).fill(0).map(() => new Array(m + 1).fill(0));
    for (let i: number = 0; i < m; i++) {
        for (let j: number = 0; j < n; j++) {
            preRow[i][j + 1] = preRow[i][j] + grid[i][j];
            preCol[j][i + 1] = preCol[j][i] + grid[i][j];
        }
    }
    for (let d: number = Math.min(m, n); d > 0; d--) {
        for (let i: number = 0; i + d <= m; i++) {
            for (let j: number = 0; j + d <= n; j++) {
                if (preRow[i][j + d] - preRow[i][j] === d &&
                    preRow[i + d - 1][j + d] - preRow[i + d - 1][j] === d &&
                    preCol[j][i + d] - preCol[j][i] === d &&
                    preCol[j + d - 1][i + d] - preCol[j + d - 1][i] === d) {
                    return d * d;
                }
            }
        }
    }
    return 0;
};

export function Solve(inputJsonElement: string): any {
    const inputValues: string[] = inputJsonElement.split("\n");
    const grid: number[][] = JSON.parse(inputValues[0]);
    return largest1BorderedSquare(grid);
}
