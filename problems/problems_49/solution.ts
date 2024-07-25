function groupAnagrams(strs: string[]): string[][] {
    const group: Map<string, string[]> = new Map();
	for (const str of strs) {
		const key: string = str.split("").sort().join("");
		if (!group.has(key)) {
			group.set(key, []);
		}
		group.get(key).push(str);
	}
	return Array.from(group.values());
};

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const strs: string[] = JSON.parse(inputValues[0]);
	return groupAnagrams(strs);
}
