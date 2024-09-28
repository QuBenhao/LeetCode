function groupAnagrams(strs: string[]): string[][] {
	const map: Map<string, string[]> = new Map();
	for (const str of strs) {
		const key: string = str.split("").sort().join("");
		if (!map.has(key)) {
			map.set(key, []);
		}
		map.get(key).push(str);
	}
	return Array.from(map.values());
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const strs: string[] = JSON.parse(inputValues[0]);
	return groupAnagrams(strs);
}
