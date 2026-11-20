function findSubtreeSizes(parent: number[], s: string): number[] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const parent: number[] = JSON.parse(inputValues[0]);
	const s: string = JSON.parse(inputValues[1]);
	return findSubtreeSizes(parent, s);
}
