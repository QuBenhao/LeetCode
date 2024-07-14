function accountsMerge(accounts: string[][]): string[][] {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const accounts: string[][] = JSON.parse(inputValues[0]);
	return accountsMerge(accounts);
}
