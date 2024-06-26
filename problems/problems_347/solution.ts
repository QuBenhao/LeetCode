function topKFrequent(nums: number[], k: number): number[] {
    
};

export function Solve(inputJsonElement: string): any {
	const splits: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(splits[0]);
	const k: number = JSON.parse(splits[1]);
	return topKFrequent(nums, k);
}
