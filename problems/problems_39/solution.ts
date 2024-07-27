function combinationSum(candidates: number[], target: number): number[][] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const candidates: number[] = JSON.parse(inputValues[0]);
	const target: number = JSON.parse(inputValues[1]);
	return combinationSum(candidates, target);
}
