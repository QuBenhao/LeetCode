function findThePrefixCommonArray(A: number[], B: number[]): number[] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const A: number[] = JSON.parse(inputValues[0]);
	const B: number[] = JSON.parse(inputValues[1]);
	return findThePrefixCommonArray(A, B);
}
