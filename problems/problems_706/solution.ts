class MyHashMap {
	map: Map<number, number>;
    constructor() {
		this.map = new Map();
    }

    put(key: number, value: number): void {
		this.map.set(key, value);
    }

    get(key: number): number {
		return this.map.has(key) ? this.map.get(key)!! : -1;
    }

    remove(key: number): void {
		this.map.delete(key);
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * var obj = new MyHashMap()
 * obj.put(key,value)
 * var param_2 = obj.get(key)
 * obj.remove(key)
 */

export function Solve(inputJsonElement: string): any {
	const splits: string[] = inputJsonElement.split("\n");
	const operators: string[] = JSON.parse(splits[0]);
	const values: any[][] = JSON.parse(splits[1]);
	const ans: any[] = [null];
	const obj: MyHashMap = new MyHashMap();
	for (let i: number = 1; i < operators.length; i++) {
		if (operators[i] == "put") {
			obj.put(values[i][0], values[i][1]);
			ans.push(null);
			continue;
		}
		if (operators[i] == "get") {
			ans.push(obj.get(values[i][0]));
			continue;
		}
		if (operators[i] == "remove") {
			obj.remove(values[i][0]);
			ans.push(null);
			continue;
		}
		ans.push(null);
	}
	return ans;
}
