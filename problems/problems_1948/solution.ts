function deleteDuplicateFolder(paths: string[][]): string[][] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const paths: string[][] = JSON.parse(inputValues[0]);
	return deleteDuplicateFolder(paths);
}
