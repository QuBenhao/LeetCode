function mapWordWeights(words: string[], weights: number[]): string {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const words: string[] = JSON.parse(inputValues[0]);
	const weights: number[] = JSON.parse(inputValues[1]);
	return mapWordWeights(words, weights);
}
