function fallingSquares(positions: number[][]): number[] {
    const points: Set<number> = new Set();
	for (const [left, size] of positions) {
		points.add(left);
		points.add(left + size - 1);
	}
	const sortedPoints: number[] = Array.from(points).sort((a, b) => a - b);
	const index: Map<number, number> = new Map();
	for (let i: number = 0; i < sortedPoints.length; i++) {
		index.set(sortedPoints[i], i);
	}
	const ans: number[] = new Array(positions.length);
	const heights: number[] = new Array(sortedPoints.length).fill(0);
	for (let i: number = 0; i < positions.length; i++) {
		const [left, size] = positions[i];
		const start: number = index.get(left);
		const end: number = index.get(left + size - 1);
		let h: number = 0;
		for (let j: number = start; j <= end; j++) {
			h = Math.max(h, heights[j]);
		}
		h += size;
		for (let j: number = start; j <= end; j++) {
			heights[j] = h;
		}
		ans[i] = Math.max(i > 0 ? ans[i - 1] : 0, h);
	}
	return ans;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const positions: number[][] = JSON.parse(inputValues[0]);
	return fallingSquares(positions);
}
