function maxConsecutiveAnswers(answerKey: string, k: number): number {
    
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const answerKey: string = JSON.parse(inputValues[0]);
	const k: number = JSON.parse(inputValues[1]);
	return maxConsecutiveAnswers(answerKey, k);
}
