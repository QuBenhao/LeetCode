function removeSubfolders(folder: string[]): string[] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const folder: string[] = JSON.parse(inputValues[0]);
	return removeSubfolders(folder);
}
