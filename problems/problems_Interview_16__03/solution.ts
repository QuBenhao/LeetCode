function intersection(start1: number[], end1: number[], start2: number[], end2: number[]): number[] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const start1: number[] = JSON.parse(inputValues[0]);
	const end1: number[] = JSON.parse(inputValues[1]);
	const start2: number[] = JSON.parse(inputValues[2]);
	const end2: number[] = JSON.parse(inputValues[3]);
	return intersection(start1, end1, start2, end2);
}
