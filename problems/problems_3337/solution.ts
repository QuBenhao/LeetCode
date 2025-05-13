function lengthAfterTransformations(s: string, t: number, nums: number[]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const s: string = JSON.parse(inputValues[0]);
	const t: number = JSON.parse(inputValues[1]);
	const nums: number[] = JSON.parse(inputValues[2]);
	return lengthAfterTransformations(s, t, nums);
}
