function matchPlayersAndTrainers(players: number[], trainers: number[]): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const players: number[] = JSON.parse(inputValues[0]);
	const trainers: number[] = JSON.parse(inputValues[1]);
	return matchPlayersAndTrainers(players, trainers);
}
