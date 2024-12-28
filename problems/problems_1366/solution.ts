function rankTeams(votes: string[]): string {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const votes: string[] = JSON.parse(inputValues[0]);
	return rankTeams(votes);
}
