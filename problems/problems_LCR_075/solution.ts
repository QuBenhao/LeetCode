function relativeSortArray(arr1: number[], arr2: number[]): number[] {
	let max: number = Math.max(...arr1);
	const counts: number[] = new Array(max + 1).fill(0);
	for (const num of arr1) {
		counts[num]++;
	}
	const res: number[] = [];
	for (const num of arr2) {
		while (counts[num] > 0) {
			res.push(num);
			counts[num]--;
		}
	}
	for (let i: number = 0; i <= max; i++) {
		while (counts[i] > 0) {
			res.push(i);
			counts[i]--;
		}
	}
	return res;
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const arr1: number[] = JSON.parse(inputValues[0]);
	const arr2: number[] = JSON.parse(inputValues[1]);
	return relativeSortArray(arr1, arr2);
}
