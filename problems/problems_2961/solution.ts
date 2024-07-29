function getGoodIndices(variables: number[][], target: number): number[] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const variables: number[][] = JSON.parse(inputValues[0]);
	const target: number = JSON.parse(inputValues[1]);
	return getGoodIndices(variables, target);
}
