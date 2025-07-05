class FindSumPairs {
    constructor(nums1: number[], nums2: number[]) {
        
    }

    add(index: number, val: number): void {
        
    }

    count(tot: number): number {
        
    }
}

/**
 * Your FindSumPairs object will be instantiated and called as such:
 * var obj = new FindSumPairs(nums1, nums2)
 * obj.add(index,val)
 * var param_2 = obj.count(tot)
 */

export function Solve(inputJsonElement: string): any {
	const inputValues: string[] = inputJsonElement.split("\n");
	const operators: string[] = JSON.parse(inputValues[0]);
	const opValues: any[][] = JSON.parse(inputValues[1]);
	const ans: any[] = [null];
	const obj: FindSumPairs = new FindSumPairs(opValues[0][0], opValues[0][1]);
	for (let i: number = 1; i < operators.length; i++) {
		if (operators[i] == "add") {
			obj.add(opValues[i][0], opValues[i][1]);
			ans.push(null);
			continue;
		}
		if (operators[i] == "count") {
			ans.push(obj.count(opValues[i][0]));
			continue;
		}
		ans.push(null);
	}
	return ans;
}
