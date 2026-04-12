function getMinDistance(nums: number[], target: number, start: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const nums: number[] = JSON.parse(inputValues[0]);
	const target: number = JSON.parse(inputValues[1]);
	const start: number = JSON.parse(inputValues[2]);
	return getMinDistance(nums, target, start);
}
