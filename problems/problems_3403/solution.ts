function answerString(word: string, numFriends: number): string {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const word: string = JSON.parse(inputValues[0]);
	const numFriends: number = JSON.parse(inputValues[1]);
	return answerString(word, numFriends);
}
