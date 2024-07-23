function relocateMarbles(nums: number[], moveFrom: number[], moveTo: number[]): number[] {
	const s: Set<number> = new Set<number>(nums);
	for (let i: number = 0; i < moveFrom.length; i++) {
		s.delete(moveFrom[i]);
		s.add(moveTo[i]);
	}
	return Array.from(s).sort((a, b) => a - b);
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	const moveFrom: number[] = JSON.parse(inputValues[1]);
	const moveTo: number[] = JSON.parse(inputValues[2]);
	return relocateMarbles(nums, moveFrom, moveTo);
}
