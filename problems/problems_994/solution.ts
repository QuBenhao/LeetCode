import {Queue} from "@datastructures-js/queue";

function orangesRotting(grid: number[][]): number {
    const m: number = grid.length, n: number = grid[0].length;
	const queue: Queue<number[]> = new Queue<number[]>();
	let fresh: number = 0, times: number = 0;
	const directions: number[][] = [[0, 1], [0, -1], [1, 0], [-1, 0]];
	for (let i: number = 0; i < m; i++) {
		for (let j: number = 0; j < n; j++) {
			if (grid[i][j] === 2) {
				queue.enqueue([i, j]);
			} else if (grid[i][j] === 1) {
				fresh++;
			}
		}
	}
	if (fresh === 0) return 0;
	while (!queue.isEmpty()) {
		times++;
		const size: number = queue.size();
		for (let i: number = 0; i < size; i++) {
			const [x, y]: number[] = queue.dequeue();
			for (const [dx, dy] of directions) {
				const nx: number = x + dx, ny: number = y + dy;
				if (nx < 0 || nx >= m || ny < 0 || ny >= n || grid[nx][ny] !== 1) continue;
				grid[nx][ny] = 2;
				fresh--;
				queue.enqueue([nx, ny]);
			}
		}
	}
	return fresh === 0 ? times - 1 : -1;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const grid: number[][] = JSON.parse(inputValues[0]);
	return orangesRotting(grid);
}
