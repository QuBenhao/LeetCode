function smallestString(s: string): string {
	const arr: string[] = s.split("");
	for (let i: number = 0; i < arr.length; i++) {
		if (arr[i] > 'a') {
			for (; i < arr.length && arr[i] > 'a'; i++) {
				arr[i] = String.fromCharCode(arr[i].charCodeAt(0) - 1);
			}
			return arr.join("");
		}
	}
	arr[arr.length - 1] = 'z';
	return arr.join("");
};

export function Solve(inputJsonElement: string): any {
	const splits: string[] = inputJsonElement.split("\n");
	const s: string = JSON.parse(splits[0]);
	return smallestString(s);
}
