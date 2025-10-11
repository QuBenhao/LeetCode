function magicalSum(m: number, k: number, nums: number[]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const m: number = JSON.parse(inputValues[0]);
	const k: number = JSON.parse(inputValues[1]);
	const nums: number[] = JSON.parse(inputValues[2]);
	return magicalSum(m, k, nums);
}
